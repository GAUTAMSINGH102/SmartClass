const form = document.querySelector("form"),
  fileInput = form.querySelector(".file-input"),
  progressArea = document.querySelector(".progress-area"),
  uploadedArea = document.querySelector(".uploaded-area");

let navbar = document.querySelector('.header .navbar');

window.onscroll = () =>{
  navbar.classList.remove('active');

  if(window.scrollY > 650){
     document.querySelector('.header').classList.add('active');
  }else{
     document.querySelector('.header').classList.remove('active');
  };
};

form.addEventListener("click", () => {
  fileInput.click();
});

fileInput.onchange = ({ target }) => {
  let file = target.files[0]; //if multiple file selected then choose only one out of it
  if (file) {
    //if file selected
    let fileName = file.name; //getting selected fileName
    if(fileName.length >=12) {
        let splitName = fileName.split('.'); 
        fileName = splitName[0].substring(0, 12) + "... ." + splitName[1];
    }
    uploadFile(fileName);
    
  }
};

function uploadFile(fileName) {

  let xhr = new XMLHttpRequest();

  xhr.open("POST", "/transcribe", true);

  xhr.upload.addEventListener("progress", ({ loaded, total }) => {
    let fileLoaded = Math.floor((loaded / total) * 100);
    let fileTotal = Math.floor(total / 1000);
    // console.log(fileLoaded, fileTotal);

    let fileSize;
    (fileTotal < 1024) ? fileSize = fileTotal + " KB" : fileSize = (loaded / (1024 * 1024)).toFixed(2) + " MB";

    let progressHTML = `<li class="row">
                            <i class="fas fa-file-alt"></i>
                            <div class="content">
                                <div class="details">
                                    <span class="name">${fileName} • Uploading</span>
                                    <span class="percent">${fileLoaded}%</span>
                                </div>
                                <div class="progress-bar">
                                    <div class="progress" style="width:${fileLoaded}%"></div>
                                </div>
                            </div>
                        </li>`;
    uploadedArea.innerHTML = "";
    progressArea.innerHTML = progressHTML;

    if(loaded == total) {
        progressArea.innerHTML = "";
        let uploadedHTML = `<li class="row">
                                <div class="content">
                                    <i class="fas fa-file-alt"></i>
                                    <div class="content">
                                        <div class="details">
                                            <span class="name">${fileName} • Uploading</span>
                                            <span class="size">${fileSize}</span>
                                        </div>
                                    </div>
                                </div>
                                <i class="fas fa-check"></i>
                            </li>`;

        uploadedArea.innerHTML = uploadedHTML;
        // uploadedArea.insertAdjacentHTML("afterbegin", uploadedHTML);
        // document.getElementById('summary_link').innerHTML = 'Summary';
        loadtranscribe(fileName)
    }

    
  });

  let formData = new FormData(form);
  console.log('formData');
  xhr.send(formData);
}

function loadtranscribe(fileName) {
  let xhr = new XMLHttpRequest();

  xhr.open("POST", "/getTranscribe", true);

  xhr.onload = function() {
    if(this.status==200) {
      console.log(this.responseText)
      transcribeText = this.responseText
      document.getElementById("transcribe").innerHTML = transcribeText;
      loadsummary(transcribeText)
      keywordsExtraction(transcribeText)
    }
    else {
      console.log("inside else")
    }
  }

  let formData = new FormData(form);
  console.log(formData);
  xhr.send(formData);
}




function loadsummary(transcribeTxt) {
  let transcribe = transcribeTxt
  let xhr = new XMLHttpRequest();

  console.log('inside summary')
  xhr.open("POST", "/summary", true);
  //Send the proper header information along with the request
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = function() {
    console.log('inside load')
    if(this.status==200) {
      console.log(this.responseText)
      summaryText = this.responseText
      document.getElementById("loadsummary").innerHTML = summaryText;

//      ttsImage = document.getElementById("ttsSummary")
//
//      ttsImage.addEventListener("click", tts(summaryText));

        document.getElementById("ttsSummary").onclick = function() {
        tts(summaryText)
        };

    }
    else {
      console.log("inside else")
    }
  }
  params = {"data":transcribe}
  console.log(params)
  xhr.send(JSON.stringify(params));
}



function keywordsExtraction(transcribeTxt) {
  let transcribe = transcribeTxt
  let xhr = new XMLHttpRequest();

  console.log('inside keywordsExtraction')
  xhr.open("POST", "/keywords", true);
  //Send the proper header information along with the request
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = function() {
    console.log('inside keywordsLoad')
    if(this.status==200) {
      console.log(this.responseText)
      keywordString = this.responseText
      youtubeRecommender(keywordString)
      bookRecommender(keywordString)
    }
    else {
      console.log("inside Keywords else")
    }
  }
  params = {"data":transcribe}
  console.log(params)
  xhr.send(JSON.stringify(params));
}



function youtubeRecommender(sourceKeywords) {
//  let sourceKeywords = sourceKeywords
  let xhr = new XMLHttpRequest();

  console.log('inside youtubeRecommender')
  xhr.open("POST", "/recommender", true);
  //Send the proper header information along with the request
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = function() {
    console.log('inside recommederLoad')
    if(this.status==200) {
      console.log(this.responseText)
      youtube_card = this.responseText
//      console.log(youtube_card)

      const container = document.getElementById('recommenderCards');

      var obj = JSON.parse(youtube_card);
//      console.log(obj)
//
//      for(var key in obj) {
//        console.log(obj[key][1])
//      }

      for(var key in obj) {
//        const card = document.createElement('div')
//        card.classList = 'recommendercards'
        const youtubeLink = (`https://www.youtube.com/watch?v=${obj[key][0]}`)
        console.log(youtubeLink)
        fileName = key.substring(0, 76) + "...";

        const content = `<div class="card">
        <a href=${youtubeLink} target="_blank">
                <img src=${obj[key][1]}>
               </a>
                <h3>${fileName}</h3>
            </div>`;

        container.innerHTML += content;
        console.log(container)
      }
    }
    else {
      console.log("inside recommender else")
    }
  }
  params = {"data":sourceKeywords}
  console.log(params)
  xhr.send(JSON.stringify(params));
}




function bookRecommender(sourceKeywords) {
//  let sourceKeywords = sourceKeywords
  let xhr = new XMLHttpRequest();

  console.log('inside bookRecommender')
  xhr.open("POST", "/bookRecommender", true);
  //Send the proper header information along with the request
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = function() {
    console.log('inside bookrecommederLoad')
    if(this.status==200) {
      console.log(this.responseText)
      book_cards = this.responseText
      console.log(book_cards)

      const bookcontainer = document.getElementById('bookRecommenderCards');

//      var book_obj = JSON.parse(book_cards);
//      console.log(obj)
//
//      for(var key in obj) {
//        console.log(obj[key][1])
//      }

      var bookobj = JSON.parse(book_cards);

      bookobj.forEach((title) => {
//        const card = document.createElement('div')
//        card.classList = 'recommendercards'

        fileName = title.substring(0, 200) + "...";

        const content = `<div class="bookcard">
                <h3>${fileName}</h3>
            </div>`;

        bookcontainer.innerHTML += content;
        console.log(bookcontainer)
      });
    }
    else {
      console.log("inside recommender else")
    }
  }
  params = {"data":sourceKeywords}
  console.log(params)
  xhr.send(JSON.stringify(params));
}


function tts(text) {
  let xhr = new XMLHttpRequest();

  console.log('inside tts')
  xhr.open("POST", "/tts", true);
  //Send the proper header information along with the request
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onload = function() {
    console.log('inside ttsload')
    if(this.status==200) {
      console.log(this.responseText)
    }
    else {
      console.log("inside tts else")
    }
  }
  params = {"data":text}
  console.log(params)
  xhr.send(JSON.stringify(params));
}

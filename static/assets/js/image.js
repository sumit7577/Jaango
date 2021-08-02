const preview = document.getElementById("previewImage0");
const preview1 = document.getElementById("previewImage1");
const preview2 = document.getElementById("previewImage2");
const preview3 = document.getElementById("previewImage3");
const preview4 = document.getElementById("previewImage4");
const preview5 = document.getElementById("previewImage5");
const preview6 = document.getElementById("previewImage6");
preview.style.display = "none";
preview1.style.display = "none";
preview2.style.display = "none";
preview3.style.display = "none";
preview4.style.display = "none";
preview5.style.display = "none";
preview6.style.display = "none";

const droop = document.getElementById("dropZoon0");
const droop1 = document.getElementById("dropZoon1");
const droop2 = document.getElementById("dropZoon2");
const droop3 = document.getElementById("dropZoon3");
const droop4 = document.getElementById("dropZoon4");
const droop5 = document.getElementById("dropZoon5");
const droop6 = document.getElementById("dropZoon6");

const file = document.getElementById("id_image")
const file1 = document.getElementById("id_image1")
const file2 = document.getElementById("id_image2")
const file3 = document.getElementById("id_image3")
const file4 = document.getElementById("id_image4")
const file5 = document.getElementById("id_image5")
const file6 = document.getElementById("id_image6")

const heading = document.getElementById("para0")
const heading1 = document.getElementById("para1");
const heading2 = document.getElementById("para2");
const heading3 = document.getElementById("para3");
const heading4 = document.getElementById("para4");
const heading5 = document.getElementById("para5");
const heading6 = document.getElementById("para6");



const imagesTypes = [
    "jpeg",
    "png",
    "jpg",
  ];
  
droop.addEventListener("click", (e) => {
    file.click();
})

file.addEventListener("change", function (event) {
    const filename = event.target.files[0];
    upload(filename);
});

function upload(fileDetail) {
    const fileReader = new FileReader();
    const fileType = fileDetail.type;
    const fileName = fileDetail.size;
    preview.style.display = "block";

    if (fileValidate(fileType, fileName)) {

        fileReader.addEventListener("load", function (e) {
            
            preview.setAttribute("src", fileReader.result);
            heading.style.display = "none";
    })
  };
    fileReader.readAsDataURL(fileDetail);

}


droop1.addEventListener("click", (e) => {
  file1.click();
})

file1.addEventListener("change", function (event) {
  const filename1 = event.target.files[0];
  upload1(filename1);
});

function upload1(fileDetail1) {
  const fileReader1 = new FileReader();
  const fileType1 = fileDetail1.type;
  const fileName1 = fileDetail1.size;
  preview1.style.display = "block";

  if (fileValidate(fileType1, fileName1)) {

      fileReader1.addEventListener("load", function (e) {
          
          preview1.setAttribute("src", fileReader1.result);
          heading1.style.display = "none";
  })
};
  fileReader1.readAsDataURL(fileDetail1);

}


droop2.addEventListener("click", (e) => {
  file2.click();
})

file2.addEventListener("change", function (event) {
  const filename2 = event.target.files[0];
  upload2(filename2);
});

function upload2(fileDetail2) {
  const fileReader2 = new FileReader();
  const fileType2 = fileDetail2.type;
  const fileName2 = fileDetail2.size;
  preview2.style.display = "block";

  if (fileValidate(fileType2, fileName2)) {

      fileReader2.addEventListener("load", function (e) {
          
          preview2.setAttribute("src", fileReader2.result);
          heading2.style.display = "none";
  })
};
  fileReader2.readAsDataURL(fileDetail2);

}


droop3.addEventListener("click", (e) => {
  file3.click();
})

file3.addEventListener("change", function (event) {
  const filename3 = event.target.files[0];
  upload3(filename3);
});

function upload3(fileDetail3) {
  const fileReader3 = new FileReader();
  const fileType3 = fileDetail3.type;
  const fileName3 = fileDetail3.size;
  preview3.style.display = "block";

  if (fileValidate(fileType3, fileName3)) {

      fileReader3.addEventListener("load", function (e) {
          
          preview3.setAttribute("src", fileReader3.result);
          heading3.style.display = "none";
  })
};
  fileReader3.readAsDataURL(fileDetail3);

}


droop4.addEventListener("click", (e) => {
  file4.click();
})

file4.addEventListener("change", function (event) {
  const filename4 = event.target.files[0];
  upload4(filename4);
});

function upload4(fileDetail4) {
  const fileReader4 = new FileReader();
  const fileType4 = fileDetail4.type;
  const fileName4 = fileDetail4.size;
  preview4.style.display = "block";

  if (fileValidate(fileType4, fileName4)) {

      fileReader4.addEventListener("load", function (e) {
          
          preview4.setAttribute("src", fileReader4.result);
          heading4.style.display = "none";
  })
};
  fileReader4.readAsDataURL(fileDetail4);

}


droop5.addEventListener("click", (e) => {
  file5.click();
})

file5.addEventListener("change", function (event) {
  const filename5 = event.target.files[0];
  upload5(filename5);
});

function upload5(fileDetail5) {
  const fileReader5 = new FileReader();
  const fileType5 = fileDetail5.type;
  const fileName5 = fileDetail5.size;
  preview5.style.display = "block";

  if (fileValidate(fileType5, fileName5)) {

      fileReader5.addEventListener("load", function (e) {
          
          preview5.setAttribute("src", fileReader5.result);
          heading5.style.display = "none";
  })
};
  fileReader5.readAsDataURL(fileDetail5);

}



droop6.addEventListener("click", (e) => {
  file6.click();
})

file6.addEventListener("change", function (event) {
  const filename6 = event.target.files[0];
  upload6(filename6);
});

function upload6(fileDetail6) {
  const fileReader6 = new FileReader();
  const fileType6 = fileDetail6.type;
  const fileName6 = fileDetail6.size;
  preview6.style.display = "block";

  if (fileValidate(fileType6, fileName6)) {

      fileReader6.addEventListener("load", function (e) {
          
          preview6.setAttribute("src", fileReader6.result);
          heading6.style.display = "none";
  })
};
  fileReader6.readAsDataURL(fileDetail6);

}

function fileValidate(fileType, fileSize) {
    // File Type Validation
    let isImage = imagesTypes.filter((type) => fileType.indexOf(`image/${type}`) !== -1);
  
    // If The Uploaded File Type Is 'jpeg'
    if (isImage[0] === 'jpeg') {
      // Add Inisde (uploadedFileIconText) The (jpg) Value
      //uploadedFileIconText.innerHTML = 'jpg';
    } else { // else
      // Add Inisde (uploadedFileIconText) The Uploaded File Type 
      //uploadedFileIconText.innerHTML = isImage[0];
    };
  
    // If The Uploaded File Is An Image
    if (isImage.length !== 0) {
      // Check, If File Size Is 2MB or Less
      if (fileSize <= 2000000) { // 2MB :)
        return true;
      } else { // Else File Size
        return alert('Please Your File Should be 2 Megabytes or Less');
      };
    } else { // Else File Type 
      return alert('Please make sure to upload An Image File Type');
    };
  };
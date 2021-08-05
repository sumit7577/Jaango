const preview = document.getElementById("previewImage0");
const preview1 = document.getElementById("previewImage1");

preview.style.display = "none";
preview1.style.display = "none";


const droop = document.getElementById("dropZoon0");
const droop1 = document.getElementById("dropZoon1");


const file = document.getElementById("id_image")
const file1 = document.getElementById("id_image1")


const heading = document.getElementById("para0")
const heading1 = document.getElementById("para1");


const imagesTypes = [
  "jpeg",
  "png",
  "jpg",
];
///feaured images logic
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

//all other images logic
droop1.addEventListener("click", (e) => {
  file1.click();
})

file1.addEventListener("change", function (event) {
  const filename1 = event.target.files;
  upload1(filename1);
});

function upload1(fileDetail1) {

  const fileReaderMain = new FileReader();
  fileReaderMain.readAsDataURL(fileDetail1[0]);
  preview1.style.display = "block";
  const fileType = fileDetail1[0].type;
  const fileName = fileDetail1[0].size;
  if (fileValidate(fileType, fileName)) {
    fileReaderMain.addEventListener("load", function (e) {
      preview1.setAttribute("src", fileReaderMain.result);
      heading1.style.display = "none";
    })
  }

  const div = document.getElementById("image");

  //for loops for handling other images
  for (let i = 1; i < fileDetail1.length; i++) {
    const fileReader = new FileReader();
    const fileType = fileDetail1[i].type;
    const fileName = fileDetail1[i].size;
    fileReader.readAsDataURL(fileDetail1[i]);
    if (fileValidate(fileType, fileName)) {
      fileReader.addEventListener("load", function (e) {
        let parentElement = document.createElement("div");
        parentElement.classList.add("imageView");
        let element = document.createElement("img");
        element.setAttribute("src", fileReader.result);
        parentElement.appendChild(element);
        div.appendChild(parentElement);
      })
    }
  }



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
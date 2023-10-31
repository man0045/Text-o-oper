const request = new Request("https://www.mozilla.org/favicon.icon",{
 method: "POST",
 body:'{"foo":"bar"}',
});


// const url = request.url;
// const method = request.method;
// const credentials = request.credentials;
// // console.log(credentials)
// const bodyUsed = request.bodyUsed;
// console.log(bodyUsed);

// fetch(request)
// .then((response) => response.blob())
// .then((blob) => {
//  Image.src = URL.createObjectURL(blob);
// });


fetch(request).then((response) =>{
 if(response.status === 200){
  return response.json();
 }else{
  throw new Error("Some thosn error");
 }
})
.then((response) => {
 console.debug(response);
})
.catch((error)=>{
 console.error(error);
});

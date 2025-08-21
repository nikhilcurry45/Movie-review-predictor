let button = document.getElementsByClassName('btn');
button[0].addEventListener('click',()=>{

//getting the text  
let text = document.getElementById('text').value;
if(text === ''){
    alert("write some text");
    location.reload();
  }

//removing objects
let header = document.getElementById('p');
header.remove();
let input = document.getElementsByClassName('inputbox');
input[0].remove();
let btn = document.getElementById('btn');
btn.remove();


//adding the upper text
upper_text = document.createElement('p')
upper_text.innerText = 'Your Feedback';
upper_text.style.color = 'white';
upper_text.style.fontSize = '30px';
upper_text.style.fontfamily = 'Arial';
document.getElementsByClassName('header')[0].appendChild(upper_text);

//review from ml ( yet to be added )
fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ review: text })
})
.then(res => res.json())
.then(data => {
    if (data.sentiment) {
        upper_text.innerText = `Prediction: ${data.sentiment}`;
    } else {
        upper_text.innerText = "Error: " + data.error;
    }
})
.catch(err => {
    upper_text.innerText = "Server error.";
    console.error(err);
});

//okay button for refresh

b = document.createElement('button');
b.innerText = 'Okay';
b.style.width = '30%';
b.style.height = '70px';
b.style.fontsize = 'large';
b.style.border = 'none';
b.style.borderRadius = '10px';
b.style.cursor = 'pointer';
b.style.background = 'rgba(108, 79, 250, 0.85)';
b.style.marginTop = '300px';
b.style.color = 'white';
b.addEventListener('mouseover',()=>{
  b.style.transform = 'scale(1.2)';
  b.style.transition = 'transform 0.2s';
})
b.addEventListener('mouseout',()=>{
 b.style.transform = 'scale(1)';
})
b.addEventListener('click',()=>{
  location.reload();
})

document.getElementsByClassName('header')[0].appendChild(b);
})
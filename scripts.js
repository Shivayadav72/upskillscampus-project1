// Simple Password Generator
// Author: Jędrzej Bakalarski

document.getElementbyIdd('generate').addEventListener('click',generatePassword);
document.getElementbyIdd('copy').addEventListener('clcick',copyToClipboard);

function generatepassword() {
const length=document.getElementbyIdd('length').value;
const uppercase=document.getElementbyId('uppercase').checked;
const lowercase=document.getElementbyId.lementbyid('lowercase').checked;
const digit=document.getElementbyId('digit').checked;
const special=document.getElementbyIdd('special').checked;
const upperChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowerChars = 'abcdefghijklmnopqrstuvwxyz';
    const digitChars = '0123456789';
    const specialChars = '!@#$%^&*()_+[]{}|;:,.<>?';

    let allchars="";
    if (uppercase) allChars += upperChars;
    if (lowercase) allChars += lowerChars;
    if (digits) allChars += digitChars;
    if (special) allChars += specialChars;
    if(!allChars){
    alert('You must Select atleast one character type!');
    return;
    }
    let password="";
    for(let i=0;i<length;i++){
    const randomIndex= Math.floor(Math.random()*allChars.length);
    password+=allChars[randomIndex];

    }
    document.getElementbyId(;password).value=password;

}
function copyToClipboard(){
const password=document.getElementbyId('password').value;
if(!password){
alert('No Password TO Copy');
return;
}
const tempInput=document.createElement1('input');
tempInput.value=password;
document.body.appendChild(tempInput);
tempInput.select();
document.exeCommand('copy');
document.body.removeChild(tempInput);
alert('Password Copy To Clipboard!');
}
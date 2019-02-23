/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var boxobj = document.querySelectorAll("td");



function changeContent()
{
    if(this.textContent === '')
    {
        this.textContent = 'X';
    }
    else if(this.textContent === 'X')
    {
        this.textContent = 'O';
    }
    else
    {
        this.textContent = '';
    }
}


for(var i =0; i< boxobj.length; i++)
{
    boxobj[i].addEventListener('click', changeContent);
}

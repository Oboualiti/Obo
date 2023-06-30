var updatebtns = document.getElementsByClassName('update-cart');
let inputid= document.getElementById('inputtext');
let cartpages = document.getElementsByClassName('cartpage');
let table = document.getElementById('table'); 
let shoppingnumbre = document.getElementById('shoppingnumbre');
let productsomme = document.getElementById('somme');
let sommetexts = document.getElementById('sommetext');

let dataall;
let dataid;

if(localStorage.pr!=null){
    dataid=JSON.parse(localStorage.pr)
}else{
    dataid=[]
}



//


if(localStorage.prall!=null){
    dataall=JSON.parse(localStorage.prall)
}else{
    dataall=[]
}

for (var i = 0 ;i< updatebtns.length; i++ ){
    updatebtns[i].addEventListener('click' , function(){
        var productId = this.dataset.product;
        var img = this.dataset.img;
        var category = this.dataset.category;
        var price = this.dataset.price;

        let newdata={
          
            img : img ,
            category : category,
            price : price,

        }


        dataid.push(productId);
        localStorage.setItem('pr',JSON.stringify(dataid));


        dataall.push(newdata);
        localStorage.setItem('prall',JSON.stringify(dataall));



        
    })
    
}


//cartpage and id of product

function getids(){
    inputid.value= dataid;
}


//delete data
function deletedata(){
    dataid.splice(0);
    dataall.splice(0);
    localStorage.clear();
}


function show(){
    let show = ``;
    for(let i=0;i<dataall.length;i++){
           show += `<tr>
           <th scope="row">${i+1} </th>
           <td> <img class="imgclass" src="${dataall[i].img}" >
                    
           </td>
           <td>${dataall[i].category} </td>
           <td>${dataall[i].price} </td>
           <td ><span id="delete" onclick=deleteelement(${i}) class="btn btn-outline-danger">حذف</span></td>
          </tr>`
            table.innerHTML= show;  
           }

}





function deleteelement(i) {
    dataid.splice(i,1);
    dataall.splice(i,1);
    localStorage.pr = JSON.stringify(dataid);
    localStorage.prall = JSON.stringify(dataall);
    x=x-1;
    localStorage.num = JSON.stringify(x);
    show();
    somme();

}

let x ;
if(localStorage.num!=null){
    x=JSON.parse(localStorage.num)
}else{
    x=0;
}



function numbreofproduct(){
    
    shoppingnumbre.innerHTML=dataall.length+1;
    x=shoppingnumbre.innerHTML;
    localStorage.setItem('num',JSON.stringify(x));
}

window.onload =  function(){
    shoppingnumbre.innerHTML=x;
}




show();




 
//somme de product

function somme(){
    let s=0;
    for(let i = 0 ;i<dataall.length;i++){
        s=s+ +dataall[i].price;
    }
    productsomme.innerHTML = s ;
    
    
}



somme();



function sommeup(){
    let s=0;
    for(let i = 0 ;i<dataall.length;i++){
        s=s+ +dataall[i].price;
    }
    sommetexts.value = s ;

}








let btncontain = document.getElementById('oga');

let btns = btncontain.getElementsByClassName('form-links');

for(let i = 0; i< btns.length;i++){
    btns[i].addEventListener("click", function(){
        let current = document.getElementsByClassName('active');
        current[0].className= current[0].className.replace(" active");
        this.className +=" active";
    })

}
 
 
 
 
 function opentab(evnt,Tab){
    let i, sugar , formlinks

        sugar = document.getElementsByClassName('sugar');
        for (i=0;i<sugar.length;i++){
            sugar[i].style.display="none";

        }
        formlinks = document.getElementsByClassName("form-links");

        for(i=0; i<formlinks.length; i++){
            formlinks[i].className=formlinks[i].className.replace("active","");
        }
        document.getElementById(Tab).style.display="block";
        evnt.currentTarget.className += "active";
}

document.getElementById("defaultOpen").click();


const Button = document.getElementById("addData");

Button.addEventListener("clicked", function(){
    let Firstname = document.getElementById("first-name")

    console.log(Firstname.innerText)
});








// function AddData(){
//     console.log("Am working fine!")
    
//     if( firstname.value != null && firstname
//     .value != ""){

//         TenantAdd();

//         // formClear();

//         firstname.focus();

        

//     }
// }

// // add data to table
// function TenantAdd(){
//     // first check if a <tbody> tag exists
//     if(Table.length==0){
//         Table.append("<tbody></tbody>");
//     }

//     //append data to the table
//     Table.append(`"<tr>"+ "<td>"+${firstname}.value + "</td>" + "<td>" + ${lastname}.value + "</td>" + "<td>" + ${Email}.value + "</td>" +  "<td>" + ${PhoneNumber}.value + "</td>" +  "<td>" + ${DueDate}.value + "</td>" +  "</tr>"`)

// }
// function formClear(){
//     $("#first-name").val("");
//     $("#last-name").val("");
//     $("#email").val("");
//     $("#phone").val("");
//     $("#due-date").val("");


// }

























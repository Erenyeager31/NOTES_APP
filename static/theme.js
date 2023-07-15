function change_theme(n){
    // let theme =  document.getElementById("theme")
    // theme.style.display = "none"

    if(n == "1"){
    document.getElementById("nav").style.backgroundColor = "rgb(48, 102, 0)"
    document.getElementById("menu").style.backgroundColor = "rgb(76, 154, 16)"
    document.getElementById("option").style.backgroundColor = "rgb(76, 154, 16)"
    document.body.style.backgroundColor = "rgb(194, 233, 164)"
    document.getElementById("list_head").style.color = "rgb(76, 154, 16)"
    document.getElementById("refresh").style.backgroundColor = "rgb(76, 154, 16)"
    document.getElementById("area_head").style.backgroundColor = "rgb(76, 154, 16)"
    document.getElementById("title").style.backgroundColor = "rgb(76, 154, 16)"
    let elements = document.getElementById("note_list").children   
    for(i=0;i<elements.length;i++)
    elements[i].style.backgroundColor = "rgb(76, 154, 16)"  
    document.getElementById("toolsbar").style.backgroundColor = "rgb(141, 225, 76)"
    }

if (n == "2"){          
    document.getElementById("nav").style.backgroundColor = "rgb(154, 3, 3)"
    document.getElementById("menu").style.backgroundColor = "rgb(154, 16, 16)"
    document.getElementById("option").style.backgroundColor = "rgb(154, 16, 16)"
    document.body.style.backgroundColor = "rgb(233, 164, 164)"
    document.getElementById("list_head").style.color = "rgb(154, 16, 16)"
    document.getElementById("refresh").style.backgroundColor = "rgb(154, 16, 16)"
    document.getElementById("area_head").style.backgroundColor = "rgb(154, 16, 16)"
    document.getElementById("title").style.backgroundColor = "rgb(154, 16, 16)"
    let elements = document.getElementById("note_list").children 
    for(i=0;i<elements.length;i++)
    elements[i].style.backgroundColor = "rgb(154, 16, 16)"
    document.getElementById("toolsbar").style.backgroundColor = "rgb(225, 76, 76)"
}
else if(n == "3"){    
    document.getElementById("nav").style.backgroundColor = "rgb(26, 0, 102)"
    document.getElementById("menu").style.backgroundColor = "rgb(34, 16, 154)"
    document.getElementById("option").style.backgroundColor = "rgb(34, 16, 154)"
    document.body.style.backgroundColor = "rgb(164, 164, 233)"
    document.getElementById("list_head").style.color = "rgb(34, 16, 154)"
    document.getElementById("refresh").style.backgroundColor = "rgb(34, 16, 154)"
    document.getElementById("area_head").style.backgroundColor = "rgb(34, 16, 154)"
    document.getElementById("title").style.backgroundColor = "rgb(34, 16, 154)"
    let elements = document.getElementById("note_list").children 
    for(i=0;i<elements.length;i++)
    elements[i].style.backgroundColor = "rgb(34, 16, 154)"
    document.getElementById("toolsbar").style.backgroundColor = "rgb(76, 96, 225)"
}

else if(n == "4"){
    //setting color of the navbar
document.getElementById("nav").style.backgroundColor = "rgb(133, 16, 154)"

//setting color of the menu
document.getElementById("menu").style.backgroundColor = "rgb(133, 16, 154)"

//seting color of the "options"
document.getElementById("option").style.backgroundColor = "rgb(133, 16, 154)"

//setting body bgcolor
document.body.style.backgroundColor = " rgb(218, 164, 233)"

//setting list_head color
document.getElementById("list_head").style.color = "rgb(120, 16, 154)"

//setting refresh color
document.getElementById("refresh").style.backgroundColor = "rgb(120, 16, 154)"

//setting bgcolor og areahead
document.getElementById("area_head").style.backgroundColor = "rgb(120, 16, 154)"

//setting id title which is an input in area_head
document.getElementById("title").style.backgroundColor = "rgb(120, 16, 154)"

//setting up the color for all the notes shown on the LHS
let elements = document.getElementById("note_list").children    //using the parent of all the notes that is "note_list" and then obtaining their children
// console.log(elements.length)
for(i=0;i<elements.length;i++) //using loop to access each children and then change their colour 
elements[i].style.backgroundColor = "rgb(120, 16, 154)"

//changing color of the toolsbar
document.getElementById("toolsbar").style.backgroundColor = "rgb(148, 76, 225)"
}

else if (n == "5"){         //ye wala
    document.getElementById("nav").style.backgroundColor = "rgb(20, 20, 20)"
    document.getElementById("menu").style.backgroundColor = "rgb(20, 20, 20)"
    document.getElementById("option").style.backgroundColor = "rgb(20, 20, 20)"
    document.body.style.backgroundColor = "rgb(155, 155, 154)"
    document.getElementById("list_head").style.color = "rgb(20, 20, 20)"
    document.getElementById("refresh").style.backgroundColor = "rgb(20, 20, 20)"
    document.getElementById("area_head").style.backgroundColor = "rgb(20, 20, 20)"
    document.getElementById("title").style.backgroundColor = "rgb(20, 20, 20)"
    let elements = document.getElementById("note_list").children 
    for(i=0;i<elements.length;i++)
    elements[i].style.backgroundColor = "rgb(20, 20, 20)"
    document.getElementById("toolsbar").style.backgroundColor = "rgb(69, 71, 67)"
}

    //collecting values to be send into the db
    // var col1 = document.getElementById("nav").style.backgroundColor
    // var col2 = document.getElementById("menu").style.backgroundColor
    // var col3 = document.body.style.backgroundColor
    // var col4 = document.getElementById("toolsbar").style.backgroundColor

    //the four major colours are retrived
}

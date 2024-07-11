
// Add event listeners to span elements
const nodeList = document.querySelectorAll("span");
nodeList.forEach((element) => {
    element.addEventListener("click", function (event) {
        const content = event.target.textContent;
        console.log(content);
    });
});



fetch("https://cdn.jsdelivr.net/npm/typo-js/dictionaries/en_US/en_US.aff")

    .then(response => response.text())
    .then(affData => {
        fetch("https://cdn.jsdelivr.net/npm/typo-js/dictionaries/en_US/en_US.dic")

            .then(response => response.text())
            .then(dicData => {
                const dictionary = new Typo("en_US", affData, dicData);

                const nodeList = document.querySelectorAll("span");
                nodeList.forEach((element) => {
                    element.addEventListener("click", function (event) {
                        const content = event.target.textContent;
                        // console.log(content);
                        var array_suggestions = dictionary.suggest(content);
                        console.log(array_suggestions);
                        const sugges = document.querySelector(".sugges")
                        const ul = document.createElement("ul")
                        sugges.innerHTML = ""

                        if (array_suggestions.length == 0) {
                            sugges.innerHTML = "No suggestion found"
                        }
                        
                        
                        array_suggestions.forEach(element => {
                            var li = document.createElement("li")
                            li.setAttribute("class" , "listofsugges")
                            li.style.fontFamily= "Calibri"
                            li.style.fontSize= "20px"
                            li.textContent = element
                            ul.appendChild(li)
                            sugges.appendChild(ul)
                        });

                        


                        const nodeList1 = document.querySelectorAll(".listofsugges");
                        nodeList1.forEach(element1 => {
                            element1.addEventListener("click", function(vis){
                                
                                const content1 = vis.target.textContent;
                                element.innerHTML = content1
                                element.style.textDecoration = "none"
                                ul.style.display = "none"
                                
                            })
                        });



                    });
                })
            });
    });




import { GoogleGenerativeAI } from "@google/generative-ai";


const API_KEY = "Your google gemini API key" ; // -----------------API------------------------//

// Access your API key (see "Set up your API key" above)
const genAI = new GoogleGenerativeAI(API_KEY);

const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });



async function run(prompt) 
{
    const content = document.querySelector(".output").innerHTML
    // const pr = jindata + "\n" + "Analyse the above document and Search for" + prompt + "Dont search in the internet tell only based on the information provided and tell whether it is said explicitly or implicitly in the document and also give the lines in the documet from where you have taken"
    const pr = content + "\n" + "Analyse the above document and Search for" + `"${prompt}"` + "Dont search in the internet tell only based on the information provided and also give the lines in the documet from where you have taken"
    // const pr = jindata + "\n" + "Analyse the above document and Search for" + prompt + "Dont search in the internet tell only based on the information provided "
    // const pr =  jindata + "\n" + "Analyse the above document and answer the questions" +  prompt + "Dont search in the internet tell only based on the information provided and also give the lines in the documet from where you have taken "

    const result = await model.generateContent(pr);
    const response = await result.response;
    const text = response.text();
    const converter = new showdown.Converter(); // Create a new showdown converter
    let htmlContent = converter.makeHtml(text); // Convert Markdown to HTML
    console.log(htmlContent); // Use console.log for debugging if needed
    document.querySelector(".aiout").innerHTML = htmlContent; // Update the HTML content
}


document.querySelector("#advbutton").addEventListener("click" , function() {
    const prompt = document.querySelector("#advser").value
    run(prompt)
})

document.querySelector(".summary").addEventListener("click", async function(){

    
    const out = document.querySelector(".output").innerHTML
    // console.log(out);
    const content = out + "Summarize the given document in detail and Dont search in the internet summarize only based on the information provided in the document in detail and give the summary in a plain text"
    document.innerHTML = "Summarising......."
    const result = await model.generateContent(content);
    
    const response = await result.response;
    const text = response.text();

    // console.log(text);

    const fe = fetch('/summarypage', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({text : text})
      })
      
      fe.then(function(res){
        console.log("successfully posted via Fetch API", res)
      })

      fe.catch(function(err){
        console.log(err.message);
      })

      setTimeout(function(){
        window.location.href = "/records"
    }, 2000)

})
  

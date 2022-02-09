let cards = document.getElementsByClassName('list-card list-card-additional-attribution list-card-additional-attribution-space list-card_not-saved');

data = []

function getInfo(){
	for(let i=0; i < cards.length; i++) {
		try{
			let price = document.getElementsByClassName('list-card-price')[i].innerText;
			let details = document.getElementsByClassName('list-card-details')[i].innerText;
			let date = document.getElementsByClassName('list-card-variable-text list-card-img-overlay')[i].innerText;
			data.push([date + ", " + price + ", " + details]);
		}
		catch(e){
			console.log("Error on element " + i)
		} 
  		
}}

window.onload = getInfo()

console.log(data)
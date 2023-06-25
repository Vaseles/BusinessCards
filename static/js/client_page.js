const texts = document.querySelectorAll('.text')
const message = document.querySelector('.copy_message')
const save = document.querySelector("#save")

// const body = document.querySelector("body")

// body.style.overflowY = 'hidden';
// body.style.height = '100vh';


//When U click on a text
for (let text of texts) {
   text.onclick = () => {
      copy(text.innerHTML)
      message.style.bottom = '10%'    //! ADD EFFECTS

      setTimeout(() => {
         message.style.bottom = '-10%'   //! REMOVE EFFECTS
      }, 1000)
   }
}

//! COPY FUNCTION
function copy(offer) {
   navigator.clipboard.writeText(offer)
}

//! CALL AND ADD CONTACT FUNCTION
save.onclick = () => {
   try {
      if (isContactsProtocolSupported()) { //! IF CONTACT SUPPORTED
         //! ADD IN CONTACT
         window.location.href = 'web+contacts:{{company.number}}' 
         console.log('contacts: protocol supported');
      } else { 
         //! CALL
         window.location.href = 'tel:{{company.number}}'
      }
   } catch (e) {
      console.error(e)
      //! CALL
      window.location.href = 'tel:{{company.number}}'
   }
}
const form__translates = document.querySelectorAll('.form__translate')

form__translates.forEach(form__translate => {
    const form__components = form__translate.querySelectorAll('.form__component')
    const buttons = form__translate.querySelectorAll('button')

    const reset_all_settings = () => {
        console.log('reset_all_settings')
        buttons.forEach(button => button.classList.remove('translate__button__selected'))
        form__components.forEach(input => input.classList.remove('translate__field__selected'))
    }

     for (let i = 0; i < form__components.length; i++) {
        buttons[i].addEventListener('click', () => {
            console.log('click')
            reset_all_settings()
            buttons[i].classList.add('translate__button__selected')
            form__components[i].classList.add('translate__field__selected')
        })
    }
})
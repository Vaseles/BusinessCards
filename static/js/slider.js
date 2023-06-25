
const left = document.querySelector('#sliderLeft')
const right = document.querySelector('#sliderRight')
const counter = document.querySelector('#sliderCounts')
const title = document.querySelector('#sliderTitle')
const image = document.querySelector('#sliderImage')

const slides = [
    {
        title: 'Quickly create a business card in your style!', 
        image: 'https://images.pexels.com/photos/342943/pexels-photo-342943.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    },{
        title: 'Convenient and simple',
        image: 'https://images.pexels.com/photos/4464438/pexels-photo-4464438.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    },
    {
        title: 'Huge functionality',
        image: 'https://images.pexels.com/photos/7660552/pexels-photo-7660552.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    },
]

let count = 0

title.innerHTML = slides[count].title
image.src = slides[count].image
counter.innerHTML = `0${count+1} _______ 0${slides.length}`

// left
left.onclick = () => {
    if (count-1 >= 0) {
        count--
        
        title.innerHTML = slides[count].title
        image.src = slides[count].image
        counter.innerHTML = `0${count+1} _______ 0${slides.length}`
    } else {
        count = slides.length - 1
        console.log(count)
         
        title.innerHTML = slides[count].title
        image.src = slides[count].image
        counter.innerHTML = `0${count+1} _______ 0${slides.length}`
    }
}

right.onclick = () => {
    if (slides.length > count+1) {
        count++
        
        title.innerHTML = slides[count].title
        image.src = slides[count].image
        counter.innerHTML = `0${count+1} _______ 0${slides.length}`
    } else {
        count = 0
         
        title.innerHTML = slides[count].title
        image.src = slides[count].image
        counter.innerHTML = `0${count+1} _______ 0${slides.length}`
    }
}
const form = document.getElementById("eventForm")
const fileInput = document.getElementById("event_image")
const formStory = document.getElementById("storyForm")
const fileInput2 = document.getElementById("story_image")
if (fileInput) {
    fileInput.addEventListener('change', () => {
        form.submit()
    });
    window.addEventListener('paste', e => {

        fileInput.files = e.clipboardData.files;
    })
} else {
    fileInput2.addEventListener('change', () => {
        formStory.submit();
    });
    window.addEventListener('paste', e => {

        fileInput2.files = e.clipboardData.files;
    })
}




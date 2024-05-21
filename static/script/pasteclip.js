const form = document.getElementById("eventForm");
const fileInput = document.getElementById("event_image");
const formStory = document.getElementById("storyForm");
const fileInput2 = document.getElementById("story_image");

const WIDTH = 600;

function handleFileInputChange(fileInput, form, storyWrapperId) {
    fileInput.addEventListener('change', (event) => {
        if (storyWrapperId) {
            displayImage(event.target.files[0], storyWrapperId);
        }
        //form.submit();
    });

    window.addEventListener('paste', (e) => {
        fileInput.files = e.clipboardData.files;
        if (storyWrapperId) {
            displayImage(fileInput.files[0], storyWrapperId);
        }
    });
}

function displayImage(file, wrapperId) {
    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = (event) => {
        const image = document.createElement("img");

        image.onload = (e) => {
            const canvas = document.createElement("canvas");
            const ratio = WIDTH / e.target.width; // calculate the aspect ratio
            canvas.width = WIDTH;
            canvas.height = e.target.height * ratio; // maintain the aspect ratio

            const context = canvas.getContext("2d");
            context.drawImage(image, 0, 0, canvas.width, canvas.height);

            const newImageUrl = context.canvas.toDataURL("image/jpeg", 1.0); // use maximum quality (1.0)

            const newImage = document.createElement("img");
            newImage.src = newImageUrl;

            const wrapper = document.getElementById(wrapperId);
            const existingImage = wrapper.querySelector("img");

            if (existingImage) {
                wrapper.removeChild(existingImage);
            }
            wrapper.appendChild(newImage);
        };

        image.src = event.target.result;
    };
}

if (fileInput) {
    handleFileInputChange(fileInput, form, "image_wrapper");
}

if (fileInput2) {
    handleFileInputChange(fileInput2, formStory, "image_wrapper");
}

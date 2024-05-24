const form = document.getElementById("eventForm");
const fileInput = document.getElementById("event_image");
const formStory = document.getElementById("storyForm");
const fileInput2 = document.getElementById("story_image");

const MAX_DIMENSION = 600;

function handleFileInputChange(fileInput, form, wrapperId) {
    fileInput.addEventListener('change', (event) => {
        if (wrapperId) {
            displayImage(event.target.files[0], wrapperId);
        }
        //form.submit(); // Uncomment if the form needs to be submitted automatically
    });

    window.addEventListener('paste', (e) => {
        if (e.clipboardData.files.length > 0) {
            fileInput.files = e.clipboardData.files;
            if (wrapperId) {
                displayImage(fileInput.files[0], wrapperId);
            }
        }
    });
}

function displayImage(file, wrapperId) {
    const reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = (event) => {
        const image = document.createElement("img");

        image.onload = () => {
            const canvas = document.createElement("canvas");
            const context = canvas.getContext("2d");

            let newWidth = image.width;
            let newHeight = image.height;

            if (newWidth > newHeight && newWidth > MAX_DIMENSION) {
                newHeight = Math.round((MAX_DIMENSION / newWidth) * newHeight);
                newWidth = MAX_DIMENSION;
            } else if (newHeight > newWidth && newHeight > MAX_DIMENSION) {
                newWidth = Math.round((MAX_DIMENSION / newHeight) * newWidth);
                newHeight = MAX_DIMENSION;
            } else if (newWidth > MAX_DIMENSION) {
                newHeight = Math.round((MAX_DIMENSION / newWidth) * newHeight);
                newWidth = MAX_DIMENSION;
            } else if (newHeight > MAX_DIMENSION) {
                newWidth = Math.round((MAX_DIMENSION / newHeight) * newWidth);
                newHeight = MAX_DIMENSION;
            }

            canvas.width = newWidth;
            canvas.height = newHeight;

            context.drawImage(image, 0, 0, newWidth, newHeight);

            const newImageUrl = canvas.toDataURL("image/jpeg", 1.0);

            const newImage = document.createElement("img");
            newImage.src = newImageUrl;

            const wrapper = document.getElementById(wrapperId);
            wrapper.innerHTML = ''; // Clear previous content
            wrapper.appendChild(newImage);
        };

        image.src = event.target.result;
    };
}

if (fileInput) {
    handleFileInputChange(fileInput, form, "image_wrapper");
}


Hi, I am happy to start this project. 9:40 10/12/2024
<input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element0" id="element0" value="{{ elements.0 }}" autofocus required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element1" id="element1" value="{{ elements.1 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element2" id="element2" value="{{ elements.2 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element3" id="element3" value="{{ elements.3 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element4" id="element4" value="{{ elements.4 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element5" id="element5" value="{{ elements.5 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element6" id="element6" value="{{ elements.6 }}" required>
                    <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element7" id="element7" value="{{ elements.7 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element8" id="element8" value="{{ elements.8 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                    type="number" name="element9" id="element9" value="{{ elements.9 }}" required>
                    # Retrieve and convert the input values to integers
            element0 = int(request.POST.get('element0'))
            element1 = int(request.POST.get('element1'))
            element2 = int(request.POST.get('element2'))
            element3 = int(request.POST.get('element3'))
            element4 = int(request.POST.get('element4'))
            element5 = int(request.POST.get('element5'))
            element6 = int(request.POST.get('element6'))
            element7 = int(request.POST.get('element7'))
            element8 = int(request.POST.get('element8'))
            element9 = int(request.POST.get('element9'))
            elements = [element0, element1, element2, element3,element4, element5, element6, element7,element8, element9]
            temp= [element0, element1, element2, element3,element4, element5, element6, element7,element8, element9]
/* sort.html*/
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'style.css' %}">
    <title>Sorting Visualization</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="sorting">
    <div class="flex justify-between">
    <form method="POST">
        {% csrf_token %}
        <h1 class="text-white text-[40px] font-serif italic extended-underline h-14">Sorting</h1>
        <select name="algorithm" id="algorithm" class="mx-14 my-7 h-10 rounded-xl text-white bg-black w-40 font-serif italic">
            <option class="font-serif" value="bubble">Bubble Sort</option>
            <option class="font-serif" value="selection">Selection Sort</option>
            <option class="font-serif" value="insertion">Insertion Sort</option>
            <option class="font-serif" value="merge">Merge Sort</option>
            <option class="font-serif" value="quick">Quick Sort</option>
            <option class="font-serif" value="heap">Heap Sort</option>
        </select>
    </div>

    <p class="text-white">Lorem ipsum dolor sit amet consectetur adipisicing elit...</p>

        <div class="flex flex-col items-center">
            <div class="flex justify-center mb-20 mt-24 container-sort">
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element0" id="element0" value="{{ elements.0 }}" autofocus required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element1" id="element1" value="{{ elements.1 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element2" id="element2" value="{{ elements.2 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element3" id="element3" value="{{ elements.3 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element4" id="element4" value="{{ elements.4 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element5" id="element5" value="{{ elements.5 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element6" id="element6" value="{{ elements.6 }}" required>
                <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element7" id="element7" value="{{ elements.7 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element8" id="element8" value="{{ elements.8 }}" required>
            <input class="elements h-16 w-16 text-3xl sortinput border-0 focus:border-none focus:ring-0 focus:outline-none text-white rounded-lg mx-2"
                type="number" name="element9" id="element9" value="{{ elements.9 }}" required> 
            </div>
            <div class="flex">
                <div class="flex flex-col px-5 items-center font-serif">
                    <input type="range" id="speed" min="1" max="1000" value="100" name="speed" class="m-4 cursor-pointer" required/>
                    <label for="speed" class="text-white text-center bg-black rounded-md w-32">
                        Speed:
                        <span id="speed-value">100</span> ms
                    </label>
                </div>
                <div class="text-white font-serif mt-5 px-5">
                    <input type="radio" name="option" value="ascending" id="ascending" class="cursor-pointer" required>
                    <label for="ascending">Ascending Order</label><br>
                    <input type="radio" name="option" value="option2" id="descending" class="cursor-pointer" required>
                    <label for="descending">Descending Order</label><br>
                </div>
            </div>
            <div class="flex justify-center my-5">
                <button type="submit" class="bg-red-600 rounded-xl text-white font-serif h-10 w-32 hover:bg-red-800 focus:bg-red-800">
                    Start Sorting
                </button>
            </div>
        </div>
    </form>
    <ul>
    {% for step in steps %}
    <li class="text-white">{{step}}</li>
    {% endfor %}
    </ul>
    <script>

        {% if steps %}
    
        const gridUnitX = 80; // Horizontal movement in pixels
    
        const gridUnitY = 70; // Vertical movement in pixels
    
        let delay = 0;  // Variable to manage the delay between animations
    
        
    
        {% for step in steps %}
    
        setTimeout(function () {
    
            // Define current and swap positions
    
            const x= {{step}};
    
            const currentPos = {{ step.0 }};
    
            const swapPos = {{ step.1 }};
    
            const swap = (swapPos - currentPos) * gridUnitX * -1; // Horizontal movement for swap element
    
            const current = swap * -1; // Horizontal movement for current element
    
        
    
            // Generate dynamic keyframes for 'current'
    
            const styleCurrent = document.createElement("style");
    
            styleCurrent.innerHTML = `
    
            @keyframes current-${currentPos}-${swapPos} {
    
                0% { transform: translate(0, 0); }
    
                30% { transform: translate(0, -${gridUnitY}px); }
    
                60% { transform: translate(${current}px, -${gridUnitY}px); }
    
                100% { transform: translate(${current}px, 0); }
    
            }`;
    
            document.head.appendChild(styleCurrent);
    
        
    
            // Generate dynamic keyframes for 'swap'
    
            const styleSwap = document.createElement("style");
    
            styleSwap.innerHTML = `
    
            @keyframes swap-${currentPos}-${swapPos} {
    
                0% { transform: translate(0, 0); }
    
                30% { transform: translate(0, ${gridUnitY}px); }
    
                60% { transform: translate(${swap}px, ${gridUnitY}px); }
    
                100% { transform: translate(${swap}px, 0); }
    
            }`;
    
            document.head.appendChild(styleSwap);
    
        
    
            // Dynamically get elements based on their current position IDs
    
            let currentElement = document.getElementById(`element${currentPos}`);
    
            let swapElement = document.getElementById(`element${swapPos}`);
    
        
    
            // Set the initial CSS positioning (absolute positioning will allow us to move elements directly)
    
            currentElement.style.position = 'relative';
    
            swapElement.style.position = 'relative';
    
        
    
            // Set the animations for the elements
    
            currentElement.style.animation = `current-${currentPos}-${swapPos} 4s ease-in-out forwards`;
    
            swapElement.style.animation = `swap-${currentPos}-${swapPos} 4s ease-in-out forwards`;
    
        
    
            // Function to update element position after animation
            const updatePosition = () => {
                // Update the position in DOM (apply the final transform to actual position)
                currentElement.style.left = `${(swapPos-currentPos)*gridUnitX}px`;
                swapElement.style.right = `-${swap}px`;
            };
        
        
                // After animation, update the element's ID to reflect the new positions in the DOM
                currentElement.id = `element${swapPos}`; 
                swapElement.id = `element${currentPos}`; 
            // Listen for the end of the animation
            currentElement.addEventListener("animationend", updatePosition);
            swapElement.addEventListener("animationend", updatePosition);
        
        }, delay);
    
        
    
        // Increase the delay for the next iteration (based on animation duration)
    
        delay += 4000;  // 4s duration for each animation step
    
        
    
        {% endfor %}
    
        {% endif %}
    
        
    
    </script>
</body>

</html>

<script>
    function toggle() {
        window.document.body.classList.toggle('dark-mode')
    }
    </script>
    <button on:click={toggle}>
        <slot/>
    </button>
    <style>
        button {
            background-color: #024D98;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 0.5rem;
            text-transform: uppercase;
            
        }
        :global(body.dark-mode) button {
            background-color: white;
            color: #024D98;
        }

        button:hover {
            cursor: pointer;
            transform: scale(1.1);
        }

    </style>
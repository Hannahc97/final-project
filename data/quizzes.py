
false = False 
true = True


QUIZZES = [
    {
        "quiz_id": 1,
        "title": "CPU, Memory and Program Execution",
        "description": "Test your knowledge on CPU, Memory and Program Execution!",
        "questions": [
            {
                "question_id": 1,
                "text": "Which of the following is NOT one of the five basic parts of a computer system?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 1, "text": "Memory", "is_correct": false},
                    {"answer_id": 2, "text": "Control Unit", "is_correct": false},
                    {"answer_id": 3, "text": "Power Supply", "is_correct": true},
                    {"answer_id": 4, "text": "Arithmetic/Logic Unit (ALU)", "is_correct": false}
                ]
            },
            {
                "question_id": 2,
                "text": "What does CPU stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 5, "text": "Central Processing Unit", "is_correct": true},
                    {"answer_id": 6, "text": "Central Peripheral Unit", "is_correct": false},
                    {"answer_id": 7, "text": "Central Performance Unit", "is_correct": false},
                    {"answer_id": 8, "text": "Central Programmable Unit", "is_correct": false}
                ]
            },
            {
                "question_id": 3,
                "text": "Which part of the CPU performs arithmetic and logical operations?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 9, "text": "Control Unit", "is_correct": false},
                    {"answer_id": 10, "text": "Arithmetic Logic Unit (ALU)", "is_correct": true},
                    {"answer_id": 11, "text": "Register", "is_correct": false},
                    {"answer_id": 12, "text": "Cache", "is_correct": false}
                ]
            },
            {
                "question_id": 4,
                "text": "What is the main function of the Control Unit in the CPU?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 13, "text": "Perform calculations", "is_correct": false},
                    {"answer_id": 14, "text": "Store data", "is_correct": false},
                    {"answer_id": 15, "text": "Direct operations of the CPU", "is_correct": true},
                    {"answer_id": 16, "text": "Handle input/output operations", "is_correct": false}
                ]
            },
            {
                "question_id": 5,
                "text": "What does RAM stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 17, "text": "Readily Accessible Memory", "is_correct": false},
                    {"answer_id": 18, "text": "Random Access Memory", "is_correct": true},
                    {"answer_id": 19, "text": "Read-Only Memory", "is_correct": false},
                    {"answer_id": 20, "text": "Rapid Action Memory", "is_correct": false}
                ]
            },
            {
                "question_id": 6,
                "text": "What does the term \"random access\" in Random Access Memory (RAM) mean?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 21, "text": "The ability to access memory locations in any order", "is_correct": true},
                    {"answer_id": 22, "text": "The ability to store data permanently", "is_correct": false},
                    {"answer_id": 23, "text": "The ability to access data sequentially", "is_correct": false},
                    {"answer_id": 24, "text": "The ability to compress data", "is_correct": false}
                ]
            },
            {
                "question_id": 7,
                "text": "What is the primary function of cache memory?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 25, "text": "Store permanent data", "is_correct": false},
                    {"answer_id": 26, "text": "Store temporary data during program execution", "is_correct": false},
                    {"answer_id": 27, "text": "Speed up access to frequently used data", "is_correct": true},
                    {"answer_id": 28, "text": "Provide long-term storage", "is_correct": false}
                ]
            },
            {
                "question_id": 8,
                "text": "What is the first step in the Fetch/Execute cycle?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 29, "text": "Instruction Decode (ID)", "is_correct": false},
                    {"answer_id": 30, "text": "Data Fetch (DF)", "is_correct": false},
                    {"answer_id": 31, "text": "Instruction Fetch (IF)", "is_correct": true},
                    {"answer_id": 32, "text": "Instruction Execution (EX)", "is_correct": false}
                ]
            },
            {
                "question_id": 9,
                "text": "What does the CPU do during the \"Fetch\" step?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 33, "text": "Retrieves an instruction from memory", "is_correct": true},
                    {"answer_id": 34, "text": "Translates the instruction into signals", "is_correct": false},
                    {"answer_id": 35, "text": "Performs the operation defined by the instruction", "is_correct": false},
                    {"answer_id": 36, "text": "Writes the result to memory or a register", "is_correct": false}
                ]
            },
            {
                "question_id": 10,
                "text": "In the machine cycle what happens during the \"Decode\" step?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 37, "text": "The instruction is executed", "is_correct": false},
                    {"answer_id": 38, "text": "The CPU retrieves an instruction from memory", "is_correct": false},
                    {"answer_id": 39, "text": "The instruction is translated into signals", "is_correct": true},
                    {"answer_id": 40, "text": "The result is stored in memory", "is_correct": false}
                ]
            },
            {
                "question_id": 11,
                "text": "What is the purpose of the Program Counter (PC) in the CPU?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 41, "text": "To store the address of the next instruction to be executed", "is_correct": true},
                    {"answer_id": 42, "text": "To count the number of instructions executed", "is_correct": false},
                    {"answer_id": 43, "text": "To manage the flow of data between registers", "is_correct": false},
                    {"answer_id": 44, "text": "To decode instructions", "is_correct": false}
                ]
            },
            {
                "question_id": 12,
                "text": "Which of the following best describes the concept of virtual memory?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 45, "text": "Using secondary storage as an extension of RAM", "is_correct": true},
                    {"answer_id": 46, "text": "Increasing the physical size of RAM", "is_correct": false},
                    {"answer_id": 47, "text": "Storing frequently accessed data in the CPU cache", "is_correct": false},
                    {"answer_id": 48, "text": "Encrypting data in RAM for security", "is_correct": false}
                ]
            },
            {
                "question_id": 13,
                "text": "Which of the following best describes the property of memory addresses in a computer system?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 49, "text": "They are sequential and start at 1", "is_correct": false},
                    {"answer_id": 50, "text": "They are sequential and start at 0", "is_correct": true},
                    {"answer_id": 51, "text": "They are non-sequential and start at 1", "is_correct": false},
                    {"answer_id": 52, "text": "They are non-sequential and start at 0", "is_correct": false}
                ]
            },
            {
                "question_id": 14,
                "text": "Which of the following operations is NOT typically performed by the ALU?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 53, "text": "Addition", "is_correct": false},
                    {"answer_id": 54, "text": "Subtraction", "is_correct": false},
                    {"answer_id": 55, "text": "Data fetching", "is_correct": true},
                    {"answer_id": 56, "text": "Logical comparisons", "is_correct": false}
                ]
            },
            {
                "question_id": 15,
                "text": "What is the primary function of the input unit in a computer system?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 57, "text": "Store data", "is_correct": false},
                    {"answer_id": 58, "text": "Perform computations", "is_correct": false},
                    {"answer_id": 59, "text": "Control other units", "is_correct": false},
                    {"answer_id": 60, "text": "Transfer data into the computer", "is_correct": true}
                ]
            },
            {
                "question_id": 16,
                "text": "Which of the following is considered a peripheral device",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 61, "text": "Control Unit", "is_correct": false},
                    {"answer_id": 62, "text": "ALU", "is_correct": false},
                    {"answer_id": 63, "text": "Keyboard", "is_correct": true},
                    {"answer_id": 64, "text": "Memory", "is_correct": false}
                ]
            },
            {
                "question_id": 17,
                "text": "What happens when data does not \"fit\" in the finite capacity of a memory location?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 65, "text": "Data is automatically compressed", "is_correct": false},
                    {"answer_id": 66, "text": "Data is stored in the next available location", "is_correct": false},
                    {"answer_id": 67, "text": "Data overflow occurs", "is_correct": true},
                    {"answer_id": 68, "text": "Data is discarded", "is_correct": false}
                ]
            },
            {
                "question_id": 18,
                "text": "What happens during the \"Execute\" step of the instruction cycle?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 69, "text": "The instruction is fetched from memory", "is_correct": false},
                    {"answer_id": 70, "text": "The instruction is translated into machine code", "is_correct": false},
                    {"answer_id": 71, "text": "The CPU carries out the operations specified by the instruction", "is_correct": true},
                    {"answer_id": 72, "text": "The result of the instruction is written back to memory or a register", "is_correct": false}
                ]
            },
            {
                "question_id": 19,
                "text": "Which of the following best describes an interrupt in the context of program execution?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 73, "text": "A mechanism to handle errors in program execution", "is_correct": false},
                    {"answer_id": 74, "text": "A signal that temporarily halts the CPU to prioritize a different task", "is_correct": true},
                    {"answer_id": 75, "text": "A method to speed up the execution of instructions", "is_correct": false},
                    {"answer_id": 76, "text": "A technique to optimize memory usage", "is_correct": false}
                ]
            },
            {
                "question_id": 20,
                "text": "In the Instruction Fetch (IF) phase, where is the instruction moved to?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 77, "text": "ALU", "is_correct": false},
                    {"answer_id": 78, "text": "Memory", "is_correct": false},
                    {"answer_id": 79, "text": "Control Unit", "is_correct": true},
                    {"answer_id": 80, "text": "Output Unit", "is_correct": false}
                ]
            },
            {
                "question_id": 21,
                "text": "In the instruction \"ADD 4000, 2000, 2080\", what does the control unit do after decoding this instruction?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 81, "text": "Adds the values in memory locations 2000 and 2080, and stores the result in the ALU", "is_correct": false},
                    {"answer_id": 82, "text": "Retrieves the data from memory locations 2000 and 2080, performs the addition, and stores the result in memory location 4000", "is_correct": true},
                    {"answer_id": 83, "text": "Fetches the instruction from memory location 4000, decodes it, and adds the values", "is_correct": false},
                    {"answer_id": 84, "text": "Stores the sum of the values in memory locations 2000 and 2080 in memory location 4000", "is_correct": false}
                ]
            },
            {
                "question_id": 22,
                "text": "What is the significance of the finite capacity of memory locations?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 85, "text": "It limits the number of instructions that can be executed by the CPU", "is_correct": false},
                    {"answer_id": 86, "text": "It ensures that data can be accessed randomly", "is_correct": false},
                    {"answer_id": 87, "text": "It restricts the size of data that can be stored in each location, potentially leading to data overflow", "is_correct": true},
                    {"answer_id": 88, "text": "It guarantees that memory is organised in a sequence of discrete locations", "is_correct": false}
                ]
            },
            {
                "question_id": 23,
                "text": "How does the concept of 'memory words' improve the efficiency of memory usage?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 89, "text": "By allowing multiple bytes to be accessed simultaneously", "is_correct": true},
                    {"answer_id": 90, "text": "By ensuring data is stored in non-contiguous memory locations", "is_correct": false},
                    {"answer_id": 91, "text": "By reducing the finite capacity limitations of individual memory locations", "is_correct": false},
                    {"answer_id": 92, "text": "By enabling faster decoding of instructions", "is_correct": false}
                ]
            },
            {
                "question_id": 24,
                "text": "What is the primary reason for the use of discrete locations in memory organisation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 93, "text": "To enhance the speed of data retrieval", "is_correct": false},
                    {"answer_id": 94, "text": "To facilitate the random access of data", "is_correct": false},
                    {"answer_id": 95, "text": "To ensure each memory location has a unique address", "is_correct": true},
                    {"answer_id": 96, "text": "To maximize the storage capacity of memory", "is_correct": false}
                ]
            },
            {
                "question_id": 25,
                "text": "What is a key characteristic of RAM that differentiates it from other types of memory?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 97, "text": "It is volatile and loses its content when power is turned off", "is_correct": true},
                    {"answer_id": 98, "text": "It stores data permanently", "is_correct": false},
                    {"answer_id": 99, "text": "It is used primarily for input/output operations", "is_correct": false},
                    {"answer_id": 100, "text": "It can only be accessed sequentially", "is_correct": false}
                ]
            },
            {
                "question_id": 26,
                "text": "During the Instruction Execution (EX) phase, what happens if the ALU encounters an undefined operation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 101, "text": "It generates a predefined result", "is_correct": false},
                    {"answer_id": 102, "text": "It skips the operation and moves to the next instruction", "is_correct": false},
                    {"answer_id": 103, "text": "It raises an exception or error", "is_correct": true},
                    {"answer_id": 104, "text": "It requests the control unit for further instructions", "is_correct": false}
                ]
            },
            {
                "question_id": 27,
                "text": "How does the ALU handle logical operations such as AND, OR, and NOT?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 105, "text": "By using arithmetic circuits", "is_correct": false},
                    {"answer_id": 106, "text": "By employing dedicated logic gates", "is_correct": true},
                    {"answer_id": 107, "text": "By fetching additional data from memory", "is_correct": false},
                    {"answer_id": 108, "text": "By interacting with the control unit for each operation", "is_correct": false}
                ]
            },
            {
                "question_id": 28,
                "text": "What would likely happen if the control unit fails to update the Program Counter (PC) after an instruction is fetched?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 109, "text": "The same instruction would be fetched repeatedly", "is_correct": true},
                    {"answer_id": 110, "text": "The next instruction would be skipped", "is_correct": false},
                    {"answer_id": 111, "text": "The ALU would perform an undefined operation", "is_correct": false},
                    {"answer_id": 112, "text": "The fetched instruction would not be decoded", "is_correct": false}
                ]
            },
            {
                "question_id": 29,
                "text": "In the context of computer memory, what is a primary benefit of hierarchical memory organisation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 113, "text": "It reduces the complexity of the control unit", "is_correct": false},
                    {"answer_id": 114, "text": "It optimizes the speed and cost of memory access", "is_correct": true},
                    {"answer_id": 115, "text": "It ensures all data fits into the fastest memory available", "is_correct": false},
                    {"answer_id": 116, "text": "It simplifies the process of data storage and retrieval", "is_correct": false}
                ]
            },
            {
                "question_id": 30,
                "text": "What is the significance of the binary object file format?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 117, "text": "It allows easy modification of program instructions", "is_correct": false},
                    {"answer_id": 118, "text": "It enables the computer to run software by interpreting binary instructions", "is_correct": true},
                    {"answer_id": 119, "text": "It increases the readability of the program for humans", "is_correct": false},
                    {"answer_id": 120, "text": "It reduces the size of the program in memory", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 2,
        "title": "Compilation Interpretation & Java Virtual Machine",
        "description": "Test your knowledge on Compilation Interpretation & Java Virtual Machine!",
        "questions":[
            {
               "question_id": 31,
                "text": "What is a high-level programming language?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 121, "text": "Machine code", "is_correct": false},
                    {"answer_id": 122, "text": "Assembly code", "is_correct": false},
                    {"answer_id": 123, "text": "Java", "is_correct": true},
                    {"answer_id": 124, "text": "Opcodes", "is_correct": false}
                ] 
            },
            {
                "question_id": 32,
                "text": "Which program converts assembly code to machine code?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 125, "text": "Compiler", "is_correct": false},
                    {"answer_id": 126, "text": "Assembler", "is_correct": true},
                    {"answer_id": 127, "text": "Linker", "is_correct": false},
                    {"answer_id": 128, "text": "Loader", "is_correct": false}
                ]
            },
            {
                "question_id": 33,
                "text": "What is the role of a linker?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 129, "text": "Converts source code to object code", "is_correct": false},
                    {"answer_id": 130, "text": "Loads programs into memory", "is_correct": false},
                    {"answer_id": 131, "text": "Combines different assembled parts into a whole", "is_correct": true},
                    {"answer_id": 132, "text": "Executes programs", "is_correct": false}
                ]
            },
            {
                "question_id": 34,
                "text": "Which of the following languages is typically compiled?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 133, "text": "JavaScript", "is_correct": false},
                    {"answer_id": 134, "text": "Python", "is_correct": false},
                    {"answer_id": 135, "text": "Java", "is_correct": false},
                    {"answer_id": 136, "text": "C++", "is_correct": true}
                ]
            },
            {
                "question_id": 35,
                "text": "What does an interpreter do?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 137, "text": "Converts source code to object code", "is_correct": false},
                    {"answer_id": 138, "text": "Follows the source code and executes it directly", "is_correct": true},
                    {"answer_id": 139, "text": "Combines different assembled parts into a whole", "is_correct": false},
                    {"answer_id": 140, "text": "Loads programs into memory", "is_correct": false}
                ]
            },
            {
                "question_id": 36,
                "text": "What is a disadvantage of interpretation?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 141, "text": "Harder than compiling", "is_correct": false},
                    {"answer_id": 142, "text": "Hardware dependent", "is_correct": false},
                    {"answer_id": 143, "text": "Slow execution", "is_correct": true},
                    {"answer_id": 144, "text": "Cannot run on different platforms", "is_correct": false}
                ]
            },
            {
                "question_id": 37,
                "text": "What does JVM stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 145, "text": "Java Visual Machine", "is_correct": false},
                    {"answer_id": 146, "text": "Java Virtual Model", "is_correct": false},
                    {"answer_id": 147, "text": "Java Virtual Machine", "is_correct": true},
                    {"answer_id": 148, "text": "Java Visual Model", "is_correct": false}
                ]
            },
            {
                "question_id": 38,
                "text": "Which language does the Java compiler translate Java source code into?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 149, "text": "Machine code", "is_correct": false},
                    {"answer_id": 150, "text": "Assembly code", "is_correct": false},
                    {"answer_id": 151, "text": "Bytecode", "is_correct": true},
                    {"answer_id": 152, "text": "High-level code", "is_correct": false}
                ]
            },
            {
                "question_id": 39,
                "text": "What is the primary advantage of Java's bytecode?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 153, "text": "Faster execution", "is_correct": false},
                    {"answer_id": 154, "text": "Platform independence", "is_correct": true},
                    {"answer_id": 155, "text": "Easier to read", "is_correct": false},
                    {"answer_id": 156, "text": "Smaller file size", "is_correct": false}
                ]
            },
            {
                "question_id": 40,
                "text": "What does JIT stand for in the context of JVM?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 157, "text": "Java Intermediate Translation", "is_correct": false},
                    {"answer_id": 158, "text": "Just-In-Time", "is_correct": true},
                    {"answer_id": 159, "text": "Java Integrated Tool", "is_correct": false},
                    {"answer_id": 160, "text": "Java Interpretation Technology", "is_correct": false}
                ]
            },
            {
                "question_id": 41,
                "text": "Which of the following is a characteristic of low-level languages?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 161, "text": "Easier for humans to read and write", "is_correct": false},
                    {"answer_id": 162, "text": "Harder for humans to read and write", "is_correct": true},
                    {"answer_id": 163, "text": "Platform independent", "is_correct": false},
                    {"answer_id": 164, "text": "Interpreted directly", "is_correct": false}
                ]
            },
            {
                "question_id": 42,
                "text": "In the compilation process, what is the role of the loader?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 165, "text": "Converts source code to object code", "is_correct": false},
                    {"answer_id": 166, "text": "Loads the program into memory at a given location", "is_correct": true},
                    {"answer_id": 167, "text": "Combines different assembled parts into a whole", "is_correct": false},
                    {"answer_id": 168, "text": "Optimizes the object code", "is_correct": false}
                ]
            },
            {
                "question_id": 43,
                "text": "Why is compilation generally more efficient than interpretation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 169, "text": "Compilation is done once for each program", "is_correct": true},
                    {"answer_id": 170, "text": "Compiled programs are easier to debug", "is_correct": false},
                    {"answer_id": 171, "text": "Interpreters are hardware dependent", "is_correct": false},
                    {"answer_id": 172, "text": "Compiled programs run slower", "is_correct": false}
                ]
            },
            {
                "question_id": 44,
                "text": "What is cross-compilation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 173, "text": "Compiler runs on the same platform as the target code", "is_correct": false},
                    {"answer_id": 174, "text": "Compiler runs on a different platform than the target code", "is_correct": true},
                    {"answer_id": 175, "text": "Interpreter runs on the same platform as the source code", "is_correct": false},
                    {"answer_id": 176, "text": "Interpreter runs on a different platform than the source code", "is_correct": false}
                ]
            },
            {
                "question_id": 45,
                "text": "Which of the following is an advantage of interpretation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 177, "text": "Faster execution", "is_correct": false},
                    {"answer_id": 178, "text": "Platform independence", "is_correct": false},
                    {"answer_id": 179, "text": "Facilitates interactive debugging and testing", "is_correct": true},
                    {"answer_id": 180, "text": "Generates object code", "is_correct": false}
                ]
            },
            {
                "question_id": 46,
                "text": "What is an intermediate language in the context of combined compilation and interpretation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 181, "text": "High-level code", "is_correct": false},
                    {"answer_id": 182, "text": "Machine code", "is_correct": false},
                    {"answer_id": 183, "text": "A language between high and low level that can be efficiently interpreted", "is_correct": true},
                    {"answer_id": 184, "text": "Assembly code", "is_correct": false}
                ]
            },
            {
                "question_id": 47,
                "text": "Why is Java considered platform-independent?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 185, "text": "It compiles directly to machine code", "is_correct": false},
                    {"answer_id": 186, "text": "It uses a single compiler for all platforms", "is_correct": false},
                    {"answer_id": 187, "text": "It compiles to bytecode that can be interpreted by JVM on any platform", "is_correct": true},
                    {"answer_id": 188, "text": "It does not require compilation", "is_correct": false}
                ]
            },
            {
                "question_id": 48,
                "text": "What is the primary function of a virtual machine?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 189, "text": "To convert high-level code to machine code", "is_correct": false},
                    {"answer_id": 190, "text": "To execute an instruction stream in software", "is_correct": true},
                    {"answer_id": 191, "text": "To manage hardware resources", "is_correct": false},
                    {"answer_id": 192, "text": "To link different parts of a program", "is_correct": false}
                ]
            },
            {
                "question_id": 49,
                "text": "How does JIT compilation improve performance?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 193, "text": "By interpreting code directly", "is_correct": false},
                    {"answer_id": 194, "text": "By pre-compiling all code", "is_correct": false},
                    {"answer_id": 195, "text": "By compiling bytecode to machine code just before execution", "is_correct": true},
                    {"answer_id": 196, "text": "By optimizing source code", "is_correct": false}
                ]
            },
            {
                "question_id": 50,
                "text": "What is the main difference between a stack machine and a register machine?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 197, "text": "Stack machines use a stack for intermediate results, register machines use registers", "is_correct": true},
                    {"answer_id": 198, "text": "Stack machines are faster than register machines", "is_correct": false},
                    {"answer_id": 199, "text": "Register machines are used in virtual machines", "is_correct": false},
                    {"answer_id": 200, "text": "Stack machines cannot handle complex expressions", "is_correct": false}
                ]
            },
            {
                "question_id": 51,
                "text": "What is the primary disadvantage of using a virtual machine for program execution?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 201, "text": "Lack of platform independence", "is_correct": false},
                    {"answer_id": 202, "text": "Increased memory usage", "is_correct": false},
                    {"answer_id": 203, "text": "Slower execution compared to native machine code", "is_correct": true},
                    {"answer_id": 204, "text": "Difficult debugging process", "is_correct": false}
                ]
            },
            {
                "question_id": 52,
                "text": "Which of the following best describes the role of the Java Runtime Environment (JRE)?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 205, "text": "Compiles Java source code to bytecode", "is_correct": false},
                    {"answer_id": 206, "text": "Executes Java bytecode using the JVM", "is_correct": true},
                    {"answer_id": 207, "text": "Translates high-level Java code to machine code", "is_correct": false},
                    {"answer_id": 208, "text": "Links different parts of a Java program", "is_correct": false}
                ]
            },
            {
                "question_id": 53,
                "text": "Why might a JIT compiler be preferred over a traditional interpreter in certain scenarios?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 209, "text": "It reduces the need for platform-specific code", "is_correct": false},
                    {"answer_id": 210, "text": "It compiles the entire program ahead of time", "is_correct": false},
                    {"answer_id": 211, "text": "It improves execution speed by compiling code at runtime", "is_correct": true},
                    {"answer_id": 212, "text": "It simplifies the source code", "is_correct": false}
                ]
            },
            {
                "question_id": 54,
                "text": "What is one key advantage of bytecode over directly compiling to machine code?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 213, "text": "Faster execution on all platforms", "is_correct": false},
                    {"answer_id": 214, "text": "Easier to read and debug", "is_correct": false},
                    {"answer_id": 215, "text": "Greater portability across different hardware architectures", "is_correct": true},
                    {"answer_id": 216, "text": "Simpler to optimize for specific hardware features", "is_correct": false}
                ]
            },
            {
                "question_id": 55,
                "text": "In the context of Java, what is the primary role of the 'javac' tool?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 217, "text": "Execute Java programs", "is_correct": false},
                    {"answer_id": 218, "text": "Compile Java source code to bytecode", "is_correct": true},
                    {"answer_id": 219, "text": "Interpret Java bytecode", "is_correct": false},
                    {"answer_id": 220, "text": "Link Java programs", "is_correct": false}
                ]
            },
            {
                "question_id": 56,
                "text": "What is a significant challenge in cross-compilation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 221, "text": "Maintaining code readability", "is_correct": false},
                    {"answer_id": 222, "text": "Ensuring code executes correctly on the target platform", "is_correct": true},
                    {"answer_id": 223, "text": "Linking object code", "is_correct": false},
                    {"answer_id": 224, "text": "Loading the program into memory", "is_correct": false}
                ]
            },
            {
                "question_id": 57,
                "text": "Why is the concept of a stack important in JVM architecture?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 225, "text": "It provides a fixed memory allocation for variables", "is_correct": false},
                    {"answer_id": 226, "text": "It allows dynamic memory management", "is_correct": false},
                    {"answer_id": 227, "text": "It supports the execution of recursive methods", "is_correct": true},
                    {"answer_id": 228, "text": "It facilitates the use of global variables", "is_correct": false}
                ]
            },
            {
                "question_id": 58,
                "text": "Which of the following JVM instruction groups is primarily responsible for method invocation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 229, "text": "Stack Operations", "is_correct": false},
                    {"answer_id": 230, "text": "Integer Arithmetic", "is_correct": false},
                    {"answer_id": 231, "text": "Branching", "is_correct": false},
                    {"answer_id": 232, "text": "Invoking a method / return from a method", "is_correct": true}
                ]
            },
            {
                "question_id": 59,
                "text": "How does the JVM ensure security during program execution?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 233, "text": "By using hardware-based encryption", "is_correct": false},
                    {"answer_id": 234, "text": "By verifying bytecode before execution", "is_correct": true},
                    {"answer_id": 235, "text": "By limiting the use of certain instructions", "is_correct": false},
                    {"answer_id": 236, "text": "By running all code in a virtual environment", "is_correct": false}
                ]
            },
            {
                "question_id": 60,
                "text": "What is a key feature of the picoJava II chip in relation to JVM?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 237, "text": "It compiles Java code directly to machine code", "is_correct": false},
                    {"answer_id": 238, "text": "It interprets Java bytecode in hardware for embedded applications", "is_correct": true},
                    {"answer_id": 239, "text": "It optimizes Java code for desktop applications", "is_correct": false},
                    {"answer_id": 240, "text": "It supports multiple high-level programming languages", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 3,
        "title": "Computer Organisation and Architecture",
        "description": "Test your knowledge on Computer Organisation and Architecture!",
        "questions":[
            {
                "question_id": 61,
                "text": "What type of memory is commonly implemented in Dynamic RAM (DRAM)?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 241, "text": "Main memory", "is_correct": true},
                    {"answer_id": 242, "text": "Read-only memory", "is_correct": false},
                    {"answer_id": 243, "text": "Cache memory", "is_correct": false},
                    {"answer_id": 244, "text": "Secondary storage", "is_correct": false}
                ]
            },
            {
                "question_id": 62,
                "text": "Which type of memory cannot be modified once it is programmed?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 245, "text": "RAM", "is_correct": false},
                    {"answer_id": 246, "text": "ROM", "is_correct": true},
                    {"answer_id": 247, "text": "EEPROM", "is_correct": false},
                    {"answer_id": 248, "text": "Cache memory", "is_correct": false}
                ]
            },
            {
                "question_id": 63,
                "text": "In the von Neumann architecture, what is stored in the instruction register?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 249, "text": "Data", "is_correct": false},
                    {"answer_id": 250, "text": "Instructions", "is_correct": true},
                    {"answer_id": 251, "text": "Addresses", "is_correct": false},
                    {"answer_id": 252, "text": "Results", "is_correct": false}
                ]
            },
            {
                "question_id": 64,
                "text": "Which I/O mechanism involves the CPU constantly checking the status of an I/O device?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 253, "text": "Interrupt Driven I/O", "is_correct": false},
                    {"answer_id": 254, "text": "Direct Memory Access (DMA)", "is_correct": false},
                    {"answer_id": 255, "text": "Programmed I/O", "is_correct": true},
                    {"answer_id": 256, "text": "SCSI I/O", "is_correct": false}
                ]
            },
            {
                "question_id": 65,
                "text": "What does DMA stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 257, "text": "Direct Machine Access", "is_correct": false},
                    {"answer_id": 258, "text": "Direct Memory Access", "is_correct": true},
                    {"answer_id": 259, "text": "Dynamic Memory Allocation", "is_correct": false},
                    {"answer_id": 260, "text": "Device Memory Access", "is_correct": false}
                ]
            },
            {
                "question_id": 66,
                "text": "Which type of system architecture features multiple processors sharing bus, clock, memory, and peripherals?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 261, "text": "Single-Processor Systems", "is_correct": false},
                    {"answer_id": 262, "text": "Multiprocessor Systems", "is_correct": true},
                    {"answer_id": 263, "text": "Clustered Systems", "is_correct": false},
                    {"answer_id": 264, "text": "Embedded Systems", "is_correct": false}
                ]
            },
            {
                "question_id": 67,
                "text": "What is the main advantage of a symmetric multiprocessor system over an asymmetric one?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 265, "text": "Increased throughput", "is_correct": false},
                    {"answer_id": 266, "text": "Lower cost", "is_correct": false},
                    {"answer_id": 267, "text": "Equal utilisation of processors", "is_correct": true},
                    {"answer_id": 268, "text": "Easier programming", "is_correct": false}
                ]
            },
            {
                "question_id": 68,
                "text": "What is a common example of a multicore system?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 269, "text": "Supercomputer", "is_correct": false},
                    {"answer_id": 270, "text": "Mainframe", "is_correct": false},
                    {"answer_id": 271, "text": "Blade server", "is_correct": true},
                    {"answer_id": 272, "text": "Laptop", "is_correct": false}
                ]
            },
            {
                "question_id": 69,
                "text": "What is the primary purpose of a device driver in a computer system?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 273, "text": "To control the CPU", "is_correct": false},
                    {"answer_id": 274, "text": "To manage memory", "is_correct": false},
                    {"answer_id": 275, "text": "To provide a uniform interface to the device", "is_correct": true},
                    {"answer_id": 276, "text": "To execute programs", "is_correct": false}
                ]
            },
            {
                "question_id": 70,
                "text": "Which storage device is typically the fastest?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 277, "text": "Hard Disk Drive (HDD)", "is_correct": false},
                    {"answer_id": 278, "text": "Solid State Drive (SSD)", "is_correct": true},
                    {"answer_id": 279, "text": "Optical Disk", "is_correct": false},
                    {"answer_id": 280, "text": "Magnetic Tape", "is_correct": false}
                ]
            },
            {
                "question_id": 71,
                "text": "What is a key characteristic of Dynamic RAM (DRAM)?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 281, "text": "Non-volatile", "is_correct": false},
                    {"answer_id": 282, "text": "Volatile", "is_correct": true},
                    {"answer_id": 283, "text": "Read-only", "is_correct": false},
                    {"answer_id": 284, "text": "Programmable", "is_correct": false}
                ]
            },
            {
                "question_id": 72,
                "text": "What role does the device controller play in a computer system?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 285, "text": "It interfaces the CPU with I/O devices", "is_correct": true},
                    {"answer_id": 286, "text": "It manages memory allocation", "is_correct": false},
                    {"answer_id": 287, "text": "It controls the execution of programs", "is_correct": false},
                    {"answer_id": 288, "text": "It handles interrupts from hardware", "is_correct": false}
                ]
            },
            {
                "question_id": 73,
                "text": "Which I/O mechanism is preferred for moving large amounts of data?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 289, "text": "Programmed I/O", "is_correct": false},
                    {"answer_id": 290, "text": "Interrupt Driven I/O", "is_correct": false},
                    {"answer_id": 291, "text": "Direct Memory Access (DMA)", "is_correct": true},
                    {"answer_id": 292, "text": "Manual Data Transfer", "is_correct": false}
                ]
            },
            {
                "question_id": 74,
                "text": "How does the CPU interact with main memory during execution?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 293, "text": "By sending and receiving data directly from the cache", "is_correct": false},
                    {"answer_id": 294, "text": "By loading instructions from main memory and storing results back to it", "is_correct": true},
                    {"answer_id": 295, "text": "By constantly polling the memory for updates", "is_correct": false},
                    {"answer_id": 296, "text": "By using secondary storage as an intermediary", "is_correct": false}
                ]
            },
            {
                "question_id": 75,
                "text": "What is the primary function of cache memory in a computer system?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 297, "text": "To store data permanently", "is_correct": false},
                    {"answer_id": 298, "text": "To hold frequently accessed data for quick retrieval", "is_correct": true},
                    {"answer_id": 299, "text": "To manage I/O operations", "is_correct": false},
                    {"answer_id": 300, "text": "To interface with peripheral devices", "is_correct": false}
                ]
            },
            {
                "question_id": 76,
                "text": "What is the primary disadvantage of Programmed I/O?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 301, "text": "It requires the CPU to be constantly busy checking I/O status", "is_correct": true},
                    {"answer_id": 302, "text": "It cannot handle high-speed devices", "is_correct": false},
                    {"answer_id": 303, "text": "It does not support interrupts", "is_correct": false},
                    {"answer_id": 304, "text": "It requires specialised hardware", "is_correct": false}
                ]
            },
            {
                "question_id": 77,
                "text": "In a multiprocessor system, what does the term 'graceful degradation' refer to?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 305, "text": "The system continues to operate even if one processor fails", "is_correct": true},
                    {"answer_id": 306, "text": "The system gradually slows down under heavy load", "is_correct": false},
                    {"answer_id": 307, "text": "The system loses data when a processor fails", "is_correct": false},
                    {"answer_id": 308, "text": "The system needs frequent maintenance", "is_correct": false}
                ]
            },
            {
                "question_id": 78,
                "text": "What is the key difference between EEPROM and ROM?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 309, "text": "EEPROM can be electrically erased and reprogrammed", "is_correct": true},
                    {"answer_id": 310, "text": "ROM is volatile while EEPROM is non-volatile", "is_correct": false},
                    {"answer_id": 311, "text": "ROM is used for main memory", "is_correct": false},
                    {"answer_id": 312, "text": "EEPROM is read-only", "is_correct": false}
                ]
            },
            {
                "question_id": 79,
                "text": "Which mechanism does the CPU use to load instructions for execution?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 313, "text": "Fetch/Decode/Execute cycle", "is_correct": true},
                    {"answer_id": 314, "text": "Direct Memory Access", "is_correct": false},
                    {"answer_id": 315, "text": "Interrupt-driven I/O", "is_correct": false},
                    {"answer_id": 316, "text": "Cache memory", "is_correct": false}
                ]
            },
            {
                "question_id": 80,
                "text": "Why are multiprocessor systems more cost-effective than single-processor systems?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 317, "text": "They use less power", "is_correct": false},
                    {"answer_id": 318, "text": "They share peripherals, storage, and power", "is_correct": true},
                    {"answer_id": 319, "text": "They require less memory", "is_correct": false},
                    {"answer_id": 320, "text": "They are easier to program", "is_correct": false}
                ]
            },
            {
                "question_id": 81,
                "text": "In the context of I/O, what does 'polling' refer to?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 321, "text": "The CPU continuously checks the status of an I/O device", "is_correct": true},
                    {"answer_id": 322, "text": "The CPU waits for an interrupt signal from an I/O device", "is_correct": false},
                    {"answer_id": 323, "text": "The I/O device sends data directly to memory", "is_correct": false},
                    {"answer_id": 324, "text": "The I/O device operates independently of the CPU", "is_correct": false}
                ]
            },
            {
                "question_id": 82,
                "text": "What is a key characteristic of the von Neumann architecture regarding memory operations?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 325, "text": "Instructions and data are stored separately", "is_correct": false},
                    {"answer_id": 326, "text": "Instructions and data share the same memory space", "is_correct": true},
                    {"answer_id": 327, "text": "Only data is stored in memory", "is_correct": false},
                    {"answer_id": 328, "text": "Instructions are executed directly from the cache", "is_correct": false}
                ]
            },
            {
                "question_id": 83,
                "text": "How does the CPU handle an interrupt signal from an I/O device?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 329, "text": "It immediately stops all operations and addresses the interrupt", "is_correct": false},
                    {"answer_id": 330, "text": "It finishes the current instruction before handling the interrupt", "is_correct": true},
                    {"answer_id": 331, "text": "It ignores the interrupt until the I/O device sends another signal", "is_correct": false},
                    {"answer_id": 332, "text": "It transfers control to a device driver to handle the interrupt", "is_correct": false}
                ]
            },
            {
                "question_id": 84,
                "text": "What is the primary benefit of Direct Memory Access (DMA) over other I/O mechanisms?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 333, "text": "It reduces the number of interrupts", "is_correct": false},
                    {"answer_id": 334, "text": "It increases the speed of data transfer", "is_correct": false},
                    {"answer_id": 335, "text": "It allows the CPU to focus on other tasks", "is_correct": false},
                    {"answer_id": 336, "text": "All of the above", "is_correct": true}
                ]
            },
            {
                "question_id": 85,
                "text": "Why is secondary storage necessary in a computer system?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 337, "text": "Main memory is volatile and limited in size", "is_correct": true},
                    {"answer_id": 338, "text": "It is faster than main memory", "is_correct": false},
                    {"answer_id": 339, "text": "It provides temporary storage for programs", "is_correct": false},
                    {"answer_id": 340, "text": "It is used for executing instructions", "is_correct": false}
                ]
            },
            {
                "question_id": 86,
                "text": "What is the role of a device driver in the context of I/O operations?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 341, "text": "It directly controls the hardware devices", "is_correct": false},
                    {"answer_id": 342, "text": "It translates I/O requests from the operating system into device-specific operations", "is_correct": true},
                    {"answer_id": 343, "text": "It manages the CPU's interactions with memory", "is_correct": false},
                    {"answer_id": 344, "text": "It handles high-speed data transfer between devices", "is_correct": false}
                ]
            },
            {
                "question_id": 87,
                "text": "What is the primary advantage of a symmetric multiprocessor (SMP) system?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 345, "text": "It allows processors to be used equally, improving load balancing", "is_correct": true},
                    {"answer_id": 346, "text": "It simplifies the programming model", "is_correct": false},
                    {"answer_id": 347, "text": "It reduces the cost of system design", "is_correct": false},
                    {"answer_id": 348, "text": "It provides better support for single-threaded applications", "is_correct": false}
                ]
            },
            {
                "question_id": 88,
                "text": "In a clustered system, what does 'high-availability' refer to?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 349, "text": "The ability to add more storage on demand", "is_correct": false},
                    {"answer_id": 350, "text": "The ability to maintain operation despite failures", "is_correct": true},
                    {"answer_id": 351, "text": "The ability to perform high-speed computations", "is_correct": false},
                    {"answer_id": 352, "text": "The ability to run on low power", "is_correct": false}
                ]
            },
            {
                "question_id": 89,
                "text": "Why is the fetch/decode/execute cycle essential in CPU operations?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 353, "text": "It allows the CPU to process instructions systematically", "is_correct": true},
                    {"answer_id": 354, "text": "It enables direct memory access", "is_correct": false},
                    {"answer_id": 355, "text": "It manages the CPU's power consumption", "is_correct": false},
                    {"answer_id": 356, "text": "It speeds up the overall processing time", "is_correct": false}
                ]
            },
            {
                "question_id": 90,
                "text": "What is the purpose of the stack in a CPU's architecture?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 357, "text": "To store frequently accessed data for quick retrieval", "is_correct": false},
                    {"answer_id": 358, "text": "To manage local variables and method calls", "is_correct": true},
                    {"answer_id": 359, "text": "To handle direct memory access operations", "is_correct": false},
                    {"answer_id": 360, "text": "To interface with I/O devices", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 4,
        "title": "Application Layer",
        "description": "Test your knowledge on the Application Layer!",
        "questions":[
            {
                "question_id": 91,
                "text": "What is the highest layer in the TCP/IP stack?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 361, "text": "Physical Layer", "is_correct": false},
                    {"answer_id": 362, "text": "Transport Layer", "is_correct": false},
                    {"answer_id": 363, "text": "Network Layer", "is_correct": false},
                    {"answer_id": 364, "text": "Application Layer", "is_correct": true}
                ]
            },
            {
                "question_id": 92,
                "text": "Which protocol is used for web communication?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 365, "text": "FTP", "is_correct": false},
                    {"answer_id": 366, "text": "SMTP", "is_correct": false},
                    {"answer_id": 367, "text": "HTTP", "is_correct": true},
                    {"answer_id": 368, "text": "DNS", "is_correct": false}
                ]
            },
            {
                "question_id": 93,
                "text": "Which protocol is used for sending emails?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 369, "text": "HTTP", "is_correct": false},
                    {"answer_id": 370, "text": "SMTP", "is_correct": true},
                    {"answer_id": 371, "text": "FTP", "is_correct": false},
                    {"answer_id": 372, "text": "DNS", "is_correct": false}
                ]
            },
            {
                "question_id": 94,
                "text": "What is the default port number for HTTP?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 373, "text": "21", "is_correct": false},
                    {"answer_id": 374, "text": "25", "is_correct": false},
                    {"answer_id": 375, "text": "80", "is_correct": true},
                    {"answer_id": 376, "text": "443", "is_correct": false}
                ]
            },
            {
                "question_id": 95,
                "text": "What does DNS stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 377, "text": "Domain Name System", "is_correct": true},
                    {"answer_id": 378, "text": "Data Network System", "is_correct": false},
                    {"answer_id": 379, "text": "Digital Network Service", "is_correct": false},
                    {"answer_id": 380, "text": "Domain Network Service", "is_correct": false}
                ]
            },
            {
                "question_id": 96,
                "text": "Which architecture involves clients and servers?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 381, "text": "P2P", "is_correct": false},
                    {"answer_id": 382, "text": "Client-Server", "is_correct": true},
                    {"answer_id": 383, "text": "Hybrid", "is_correct": false},
                    {"answer_id": 384, "text": "Distributed", "is_correct": false}
                ]
            },
            {
                "question_id": 97,
                "text": "What does SMTP stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 385, "text": "Simple Mail Transfer Protocol", "is_correct": true},
                    {"answer_id": 386, "text": "Simple Mail Transmission Protocol", "is_correct": false},
                    {"answer_id": 387, "text": "Secure Mail Transfer Protocol", "is_correct": false},
                    {"answer_id": 388, "text": "Secure Mail Transmission Protocol", "is_correct": false}
                ]
            },
            {
                "question_id": 98,
                "text": "What type of IP address does a server in a client-server architecture usually have?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 389, "text": "Dynamic IP address", "is_correct": false},
                    {"answer_id": 390, "text": "Temporary IP address", "is_correct": false},
                    {"answer_id": 391, "text": "Permanent IP address", "is_correct": true},
                    {"answer_id": 392, "text": "Local IP address", "is_correct": false}
                ]
            },
            {
                "question_id": 99,
                "text": "Which HTTP method is used to request data from a specified resource?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 393, "text": "POST", "is_correct": false},
                    {"answer_id": 394, "text": "GET", "is_correct": true},
                    {"answer_id": 395, "text": "PUT", "is_correct": false},
                    {"answer_id": 396, "text": "DELETE", "is_correct": false}
                ]
            },
            {
                "question_id": 100,
                "text": "What is the main purpose of a domain name in DNS?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 397, "text": "To identify the MAC address of a host", "is_correct": false},
                    {"answer_id": 398, "text": "To translate human-readable names into IP addresses", "is_correct": true},
                    {"answer_id": 399, "text": "To manage email delivery", "is_correct": false},
                    {"answer_id": 400, "text": "To secure network communications", "is_correct": false}
                ]
            },
            {
                "question_id": 101,
                "text": "Which transport protocol provides reliable data transfer for HTTP?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 401, "text": "UDP", "is_correct": false},
                    {"answer_id": 402, "text": "TCP", "is_correct": true},
                    {"answer_id": 403, "text": "ICMP", "is_correct": false},
                    {"answer_id": 404, "text": "ARP", "is_correct": false}
                ]
            },
            {
                "question_id": 102,
                "text": "In a P2P architecture, how do peers typically communicate?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 405, "text": "Through a central server", "is_correct": false},
                    {"answer_id": 406, "text": "Directly with each other", "is_correct": true},
                    {"answer_id": 407, "text": "Using a proxy server", "is_correct": false},
                    {"answer_id": 408, "text": "Via DNS servers", "is_correct": false}
                ]
            },
            {
                "question_id": 103,
                "text": "What is the function of a socket in network communication?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 409, "text": "To store network addresses", "is_correct": false},
                    {"answer_id": 410, "text": "To manage hardware interfaces", "is_correct": false},
                    {"answer_id": 411, "text": "To act as an endpoint for sending and receiving data", "is_correct": true},
                    {"answer_id": 412, "text": "To translate domain names into IP addresses", "is_correct": false}
                ]
            },
            {
                "question_id": 104,
                "text": "What is a common use of port 443?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 413, "text": "Sending emails", "is_correct": false},
                    {"answer_id": 414, "text": "Secure web traffic (HTTPS)", "is_correct": true},
                    {"answer_id": 415, "text": "File transfers", "is_correct": false},
                    {"answer_id": 416, "text": "DNS queries", "is_correct": false}
                ]
            },
            {
                "question_id": 105,
                "text": "Which of the following is a key characteristic of HTTP/1.1?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 417, "text": "Non-persistent connections", "is_correct": false},
                    {"answer_id": 418, "text": "Persistent connections", "is_correct": true},
                    {"answer_id": 419, "text": "Connectionless protocol", "is_correct": false},
                    {"answer_id": 420, "text": "Designed for video streaming", "is_correct": false}
                ]
            },
            {
                "question_id": 106,
                "text": "What is the purpose of the Mail Access Protocol?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 421, "text": "To send emails between mail servers", "is_correct": false},
                    {"answer_id": 422, "text": "To retrieve emails from mail servers", "is_correct": true},
                    {"answer_id": 423, "text": "To secure email communications", "is_correct": false},
                    {"answer_id": 424, "text": "To translate email addresses", "is_correct": false}
                ]
            },
            {
                "question_id": 107,
                "text": "Which DNS record type is used to map a hostname to an IP address?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 425, "text": "CNAME", "is_correct": false},
                    {"answer_id": 426, "text": "MX", "is_correct": false},
                    {"answer_id": 427, "text": "A", "is_correct": true},
                    {"answer_id": 428, "text": "NS", "is_correct": false}
                ]
            },
            {
                "question_id": 108,
                "text": "What does the 'GET' method do in an HTTP request?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 429, "text": "Submits data to be processed", "is_correct": false},
                    {"answer_id": 430, "text": "Requests data from a specified resource", "is_correct": true},
                    {"answer_id": 431, "text": "Deletes the specified resource", "is_correct": false},
                    {"answer_id": 432, "text": "Establishes a tunnel to the server", "is_correct": false}
                ]
            },
            {
                "question_id": 109,
                "text": "Which protocol is primarily used for resolving domain names to IP addresses?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 433, "text": "HTTP", "is_correct": false},
                    {"answer_id": 434, "text": "SMTP", "is_correct": false},
                    {"answer_id": 435, "text": "DNS", "is_correct": true},
                    {"answer_id": 436, "text": "FTP", "is_correct": false}
                ]
            },
            {
                "question_id": 110,
                "text": "What is a key advantage of the P2P architecture?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 437, "text": "Simplified management", "is_correct": false},
                    {"answer_id": 438, "text": "Centralised control", "is_correct": false},
                    {"answer_id": 439, "text": "Self-scalability", "is_correct": true},
                    {"answer_id": 440, "text": "Fixed IP addresses for peers", "is_correct": false}
                ]
            },
            {
                "question_id": 111,
                "text": "How does the DNS hierarchy improve scalability and reliability?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 441, "text": "By centralising all DNS queries to a single server", "is_correct": false},
                    {"answer_id": 442, "text": "By distributing the database across multiple servers", "is_correct": true},
                    {"answer_id": 443, "text": "By using a peer-to-peer architecture for DNS resolution", "is_correct": false},
                    {"answer_id": 444, "text": "By caching all DNS records on client machines", "is_correct": false}
                ]
            },
            {
                "question_id": 112,
                "text": "What is the role of the authoritative DNS server?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 445, "text": "To store the primary DNS records for a domain", "is_correct": true},
                    {"answer_id": 446, "text": "To forward DNS queries to the root DNS server", "is_correct": false},
                    {"answer_id": 447, "text": "To handle local DNS queries within an ISP", "is_correct": false},
                    {"answer_id": 448, "text": "To cache DNS records for faster resolution", "is_correct": false}
                ]
            },
            {
                "question_id": 113,
                "text": "Which component in the email system is responsible for storing incoming messages?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 449, "text": "SMTP server", "is_correct": false},
                    {"answer_id": 450, "text": "Mailbox", "is_correct": true},
                    {"answer_id": 451, "text": "User agent", "is_correct": false},
                    {"answer_id": 452, "text": "Mail queue", "is_correct": false}
                ]
            },
            {
                "question_id": 114,
                "text": "What is a primary benefit of using persistent HTTP connections?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 453, "text": "Reduced latency for multiple requests", "is_correct": true},
                    {"answer_id": 454, "text": "Enhanced security for data transmission", "is_correct": false},
                    {"answer_id": 455, "text": "Simplified server-side processing", "is_correct": false},
                    {"answer_id": 456, "text": "Lower memory usage on the client side", "is_correct": false}
                ]
            },
            {
                "question_id": 115,
                "text": "In the context of HTTP, what does 'stateless' mean?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 457, "text": "The server maintains the state of each client session", "is_correct": false},
                    {"answer_id": 458, "text": "The server does not maintain any information about past client requests", "is_correct": true},
                    {"answer_id": 459, "text": "The client stores all state information", "is_correct": false},
                    {"answer_id": 460, "text": "The server uses cookies to track client sessions", "is_correct": false}
                ]
            },
            {
                "question_id": 116,
                "text": "Why is TCP preferred over UDP for HTTP communication?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 461, "text": "TCP is faster than UDP", "is_correct": false},
                    {"answer_id": 462, "text": "TCP provides reliable data transfer", "is_correct": true},
                    {"answer_id": 463, "text": "UDP does not support large data transfers", "is_correct": false},
                    {"answer_id": 464, "text": "UDP is not compatible with HTTP", "is_correct": false}
                ]
            },
            {
                "question_id": 117,
                "text": "What is a significant drawback of using non-persistent HTTP connections?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 465, "text": "Increased server processing time", "is_correct": false},
                    {"answer_id": 466, "text": "Higher latency due to multiple TCP handshakes", "is_correct": true},
                    {"answer_id": 467, "text": "Greater security risks", "is_correct": false},
                    {"answer_id": 468, "text": "Incompatibility with modern browsers", "is_correct": false}
                ]
            },
            {
                "question_id": 118,
                "text": "Which SMTP command is used to start the transfer of the message body?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 469, "text": "HELO", "is_correct": false},
                    {"answer_id": 470, "text": "MAIL FROM", "is_correct": false},
                    {"answer_id": 471, "text": "RCPT TO", "is_correct": false},
                    {"answer_id": 472, "text": "DATA", "is_correct": true}
                ]
            },
            {
                "question_id": 119,
                "text": "What does a Type MX DNS record specify?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 473, "text": "The IP address of a host", "is_correct": false},
                    {"answer_id": 474, "text": "The mail server for a domain", "is_correct": true},
                    {"answer_id": 475, "text": "The canonical name for an alias", "is_correct": false},
                    {"answer_id": 476, "text": "The authoritative name server for a domain", "is_correct": false}
                ]
            },
            {
                "question_id": 120,
                "text": "Why might an organisation prefer to use IMAP over POP3 for email retrieval?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 477, "text": "IMAP is more secure than POP3", "is_correct": false},
                    {"answer_id": 478, "text": "IMAP keeps all messages on the server, allowing access from multiple devices", "is_correct": true},
                    {"answer_id": 479, "text": "IMAP is faster than POP3", "is_correct": false},
                    {"answer_id": 480, "text": "IMAP allows for better spam filtering", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 5,
        "title": "Transport Layer",
        "description": "Test your knowledge on the Transport Layer!",
        "questions":[
            {
                "question_id": 121,
                "text": "What does UDP stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 481, "text": "User Datagram Protocol", "is_correct": true},
                    {"answer_id": 482, "text": "Uniform Data Protocol", "is_correct": false},
                    {"answer_id": 483, "text": "Unified Datagram Protocol", "is_correct": false},
                    {"answer_id": 484, "text": "User Data Protocol", "is_correct": false}
                ]
            },
            {
                "question_id": 122,
                "text": "What does TCP stand for?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 485, "text": "Transmission Control Protocol", "is_correct": true},
                    {"answer_id": 486, "text": "Transport Control Protocol", "is_correct": false},
                    {"answer_id": 487, "text": "Transfer Control Protocol", "is_correct": false},
                    {"answer_id": 488, "text": "Transaction Control Protocol", "is_correct": false}
                ]
            },
            {
                "question_id": 123,
                "text": "Which layer provides logical communication between application processes running on different hosts?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 489, "text": "Physical Layer", "is_correct": false},
                    {"answer_id": 490, "text": "Link Layer", "is_correct": false},
                    {"answer_id": 491, "text": "Network Layer", "is_correct": false},
                    {"answer_id": 492, "text": "Transport Layer", "is_correct": true}
                ]
            },
            {
                "question_id": 124,
                "text": "Which transport protocol provides reliable, in-order delivery?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 493, "text": "UDP", "is_correct": false},
                    {"answer_id": 494, "text": "IP", "is_correct": false},
                    {"answer_id": 495, "text": "TCP", "is_correct": true},
                    {"answer_id": 496, "text": "HTTP", "is_correct": false}
                ]
            },
            {
                "question_id": 125,
                "text": "Which transport protocol is connectionless and provides best-effort delivery?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 497, "text": "TCP", "is_correct": false},
                    {"answer_id": 498, "text": "UDP", "is_correct": true},
                    {"answer_id": 499, "text": "FTP", "is_correct": false},
                    {"answer_id": 500, "text": "SMTP", "is_correct": false}
                ]
            },
            {
                "question_id": 126,
                "text": "What is the primary purpose of a port number in networking?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 501, "text": "To identify the IP address of a host", "is_correct": false},
                    {"answer_id": 502, "text": "To identify a specific process or service on a host", "is_correct": true},
                    {"answer_id": 503, "text": "To encrypt data", "is_correct": false},
                    {"answer_id": 504, "text": "To route data between networks", "is_correct": false}
                ]
            },
            {
                "question_id": 127,
                "text": "Which protocol uses port 80 by default?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 505, "text": "FTP", "is_correct": false},
                    {"answer_id": 506, "text": "SMTP", "is_correct": false},
                    {"answer_id": 507, "text": "HTTP", "is_correct": true},
                    {"answer_id": 508, "text": "DNS", "is_correct": false}
                ]
            },
            {
                "question_id": 128,
                "text": "Which layer is responsible for multiplexing and demultiplexing in networking?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 509, "text": "Application Layer", "is_correct": false},
                    {"answer_id": 510, "text": "Transport Layer", "is_correct": true},
                    {"answer_id": 511, "text": "Network Layer", "is_correct": false},
                    {"answer_id": 512, "text": "Link Layer", "is_correct": false}
                ]
            },
            {
                "question_id": 129,
                "text": "What is the size of the UDP header?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 513, "text": "8 bytes", "is_correct": true},
                    {"answer_id": 514, "text": "16 bytes", "is_correct": false},
                    {"answer_id": 515, "text": "20 bytes", "is_correct": false},
                    {"answer_id": 516, "text": "32 bytes", "is_correct": false}
                ]
            },
            {
                "question_id": 130,
                "text": "Which field in a TCP segment header is used to acknowledge the receipt of data?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 517, "text": "Sequence Number", "is_correct": false},
                    {"answer_id": 518, "text": "Source Port", "is_correct": false},
                    {"answer_id": 519, "text": "Acknowledgment Number", "is_correct": true},
                    {"answer_id": 520, "text": "Destination Port", "is_correct": false}
                ]
            },
            {
                "question_id": 131,
                "text": "Which transport protocol is typically used for streaming multimedia applications?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 521, "text": "TCP", "is_correct": false},
                    {"answer_id": 522, "text": "FTP", "is_correct": false},
                    {"answer_id": 523, "text": "SMTP", "is_correct": false},
                    {"answer_id": 524, "text": "UDP", "is_correct": true}
                ]
            },
            {
                "question_id": 132,
                "text": "What does a TCP three-way handshake involve?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 525, "text": "SYN, ACK, SYN-ACK", "is_correct": false},
                    {"answer_id": 526, "text": "SYN, SYN-ACK, ACK", "is_correct": true},
                    {"answer_id": 527, "text": "ACK, SYN-ACK, SYN", "is_correct": false},
                    {"answer_id": 528, "text": "SYN-ACK, SYN, ACK", "is_correct": false}
                ]
            },
            {
                "question_id": 133,
                "text": "Which protocol uses the 'best effort' delivery model?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 529, "text": "TCP", "is_correct": false},
                    {"answer_id": 530, "text": "UDP", "is_correct": true},
                    {"answer_id": 531, "text": "HTTP", "is_correct": false},
                    {"answer_id": 532, "text": "FTP", "is_correct": false}
                ]
            },
            {
                "question_id": 134,
                "text": "What is the primary function of the TCP flow control mechanism?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 533, "text": "To ensure packets arrive in order", "is_correct": false},
                    {"answer_id": 534, "text": "To prevent the sender from overwhelming the receiver", "is_correct": true},
                    {"answer_id": 535, "text": "To encrypt data during transmission", "is_correct": false},
                    {"answer_id": 536, "text": "To verify the integrity of data", "is_correct": false}
                ]
            },
            {
                "question_id": 135,
                "text": "What is multiplexing in the context of the transport layer?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 537, "text": "Combining multiple data streams into one", "is_correct": true},
                    {"answer_id": 538, "text": "Splitting data into smaller segments", "is_correct": false},
                    {"answer_id": 539, "text": "Directing data to the correct application", "is_correct": false},
                    {"answer_id": 540, "text": "Ensuring data integrity", "is_correct": false}
                ]
            },
            {
                "question_id": 136,
                "text": "Which type of multiplexing is used by TCP?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 541, "text": "Time Division Multiplexing (TDM)", "is_correct": false},
                    {"answer_id": 542, "text": "Frequency Division Multiplexing (FDM)", "is_correct": false},
                    {"answer_id": 543, "text": "Port-based multiplexing", "is_correct": true},
                    {"answer_id": 544, "text": "Wave Division Multiplexing (WDM)", "is_correct": false}
                ]
            },
            {
                "question_id": 137,
                "text": "What mechanism does UDP use to detect errors in transmitted segments?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 545, "text": "Checksum", "is_correct": true},
                    {"answer_id": 546, "text": "Sequence Number", "is_correct": false},
                    {"answer_id": 547, "text": "Acknowledgment Number", "is_correct": false},
                    {"answer_id": 548, "text": "Flow Control", "is_correct": false}
                ]
            },
            {
                "question_id": 138,
                "text": "Which field in a UDP segment helps to identify the receiving application?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 549, "text": "Source Port", "is_correct": false},
                    {"answer_id": 550, "text": "Destination Port", "is_correct": true},
                    {"answer_id": 551, "text": "Length", "is_correct": false},
                    {"answer_id": 552, "text": "Checksum", "is_correct": false}
                ]
            },
            {
                "question_id": 139,
                "text": "How does TCP handle segment retransmission in case of packet loss?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 553, "text": "Using the checksum", "is_correct": false},
                    {"answer_id": 554, "text": "Using sequence numbers and acknowledgment numbers", "is_correct": true},
                    {"answer_id": 555, "text": "Using flow control", "is_correct": false},
                    {"answer_id": 556, "text": "Using encryption", "is_correct": false}
                ]
            },
            {
                "question_id": 140,
                "text": "What is the primary difference between TCP and UDP in terms of reliability?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 557, "text": "TCP is reliable, UDP is not", "is_correct": true},
                    {"answer_id": 558, "text": "UDP is reliable, TCP is not", "is_correct": false},
                    {"answer_id": 559, "text": "Both are equally reliable", "is_correct": false},
                    {"answer_id": 560, "text": "Neither provide reliability", "is_correct": false}
                ]
            },
            {
                "question_id": 141,
                "text": "What additional mechanism does RDT 3.0 introduce to handle packet loss?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 561, "text": "Sequence numbers", "is_correct": false},
                    {"answer_id": 562, "text": "Acknowledgments", "is_correct": false},
                    {"answer_id": 563, "text": "Countdown timer", "is_correct": true},
                    {"answer_id": 564, "text": "Checksum", "is_correct": false}
                ]
            },
            {
                "question_id": 142,
                "text": "How does TCP's fast retransmit mechanism improve performance?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 565, "text": "By reducing the size of the segments", "is_correct": false},
                    {"answer_id": 566, "text": "By retransmitting the segment before the timer expires if duplicate ACKs are received", "is_correct": true},
                    {"answer_id": 567, "text": "By increasing the window size", "is_correct": false},
                    {"answer_id": 568, "text": "By reducing the need for acknowledgments", "is_correct": false}
                ]
            },
            {
                "question_id": 143,
                "text": "What is the purpose of the window size parameter in TCP?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 569, "text": "To control the flow of data", "is_correct": true},
                    {"answer_id": 570, "text": "To encrypt the data", "is_correct": false},
                    {"answer_id": 571, "text": "To verify data integrity", "is_correct": false},
                    {"answer_id": 572, "text": "To manage port numbers", "is_correct": false}
                ]
            },
            {
                "question_id": 144,
                "text": "What happens during the SYN flooding attack in the context of TCP?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 573, "text": "Multiple SYN requests are sent to overwhelm the server", "is_correct": true},
                    {"answer_id": 574, "text": "Multiple ACKs are sent to confuse the server", "is_correct": false},
                    {"answer_id": 575, "text": "Multiple FIN requests are sent to close the connection", "is_correct": false},
                    {"answer_id": 576, "text": "Multiple RST requests are sent to reset the connection", "is_correct": false}
                ]
            },
            {
                "question_id": 145,
                "text": "How does TCP ensure data is delivered in the correct order?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 577, "text": "By using port numbers", "is_correct": false},
                    {"answer_id": 578, "text": "By using sequence numbers", "is_correct": true},
                    {"answer_id": 579, "text": "By using checksums", "is_correct": false},
                    {"answer_id": 580, "text": "By using timers", "is_correct": false}
                ]
            },
            {
                "question_id": 146,
                "text": "Which transport protocol is typically used for DNS queries?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 581, "text": "TCP", "is_correct": false},
                    {"answer_id": 582, "text": "FTP", "is_correct": false},
                    {"answer_id": 583, "text": "SMTP", "is_correct": false},
                    {"answer_id": 584, "text": "UDP", "is_correct": true}
                ]
            },
            {
                "question_id": 147,
                "text": "What is the key difference between TCP and UDP multiplexing?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 585, "text": "TCP uses connection-oriented multiplexing; UDP uses connectionless multiplexing", "is_correct": true},
                    {"answer_id": 586, "text": "TCP uses port numbers; UDP does not", "is_correct": false},
                    {"answer_id": 587, "text": "UDP uses sequence numbers; TCP does not", "is_correct": false},
                    {"answer_id": 588, "text": "TCP uses a checksum; UDP does not", "is_correct": false}
                ]
            },
            {
                "question_id": 148,
                "text": "In TCP, what does the sequence number represent?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 589, "text": "The total number of segments sent", "is_correct": false},
                    {"answer_id": 590, "text": "The byte stream number of the first byte in the segment", "is_correct": true},
                    {"answer_id": 591, "text": "The port number of the destination", "is_correct": false},
                    {"answer_id": 592, "text": "The total size of the segment", "is_correct": false}
                ]
            },
            {
                "question_id": 149,
                "text": "Why does UDP have a smaller header size compared to TCP?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 593, "text": "UDP does not provide reliability, ordering, or flow control", "is_correct": true},
                    {"answer_id": 594, "text": "UDP does not use port numbers", "is_correct": false},
                    {"answer_id": 595, "text": "UDP does not use IP addresses", "is_correct": false},
                    {"answer_id": 596, "text": "UDP does not use checksums", "is_correct": false}
                ]
            },
            {
                "question_id": 150,
                "text": "What is the purpose of the TCP three-way handshake?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 597, "text": "To establish a connection and synchronize sequence numbers", "is_correct": true},
                    {"answer_id": 598, "text": "To encrypt data", "is_correct": false},
                    {"answer_id": 599, "text": "To terminate a connection", "is_correct": false},
                    {"answer_id": 600, "text": "To multiplex data streams", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 6,
        "title": "Binary trees",
        "description": "Test your knowledge on Binary trees!",
        "questions":[
            {
                "question_id": 151,
                "text": "What is a binary tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 601, "text": "A tree with each node having up to three children", "is_correct": false},
                    {"answer_id": 602, "text": "A tree with each node having up to two children", "is_correct": true},
                    {"answer_id": 603, "text": "A tree with each node having one child", "is_correct": false},
                    {"answer_id": 604, "text": "A tree with no children", "is_correct": false}
                ]
            },
            {
                "question_id": 152,
                "text": "In a binary search tree, where are nodes with values less than the parent node placed?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 605, "text": "Right child", "is_correct": false},
                    {"answer_id": 606, "text": "Left child", "is_correct": true},
                    {"answer_id": 607, "text": "Root node", "is_correct": false},
                    {"answer_id": 608, "text": "Leaf node", "is_correct": false}
                ]
            },
            {
                "question_id": 153,
                "text": "Which of the following is an application of a binary search tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 609, "text": "Storing unsorted data", "is_correct": false},
                    {"answer_id": 610, "text": "Organizing a file system", "is_correct": true},
                    {"answer_id": 611, "text": "Network protocols", "is_correct": false},
                    {"answer_id": 612, "text": "Weather prediction", "is_correct": false}
                ]
            },
            {
                "question_id": 154,
                "text": "In a binary search tree, which traversal method visits nodes in sorted order?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 613, "text": "Preorder", "is_correct": false},
                    {"answer_id": 614, "text": "Inorder", "is_correct": true},
                    {"answer_id": 615, "text": "Postorder", "is_correct": false},
                    {"answer_id": 616, "text": "Level order", "is_correct": false}
                ]
            },
            {
                "question_id": 155,
                "text": "What is the time complexity of searching in a balanced binary search tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 617, "text": "O(n)", "is_correct": false},
                    {"answer_id": 618, "text": "O(n^2)", "is_correct": false},
                    {"answer_id": 619, "text": "O(log n)", "is_correct": true},
                    {"answer_id": 620, "text": "O(1)", "is_correct": false}
                ]
            },
            {
                "question_id": 156,
                "text": "Which node is the root in a binary search tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 621, "text": "The first node inserted", "is_correct": true},
                    {"answer_id": 622, "text": "The last node inserted", "is_correct": false},
                    {"answer_id": 623, "text": "The middle node", "is_correct": false},
                    {"answer_id": 624, "text": "The largest node", "is_correct": false}
                ]
            },
            {
                "question_id": 157,
                "text": "What is the height of a tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 625, "text": "Number of edges", "is_correct": false},
                    {"answer_id": 626, "text": "Number of nodes", "is_correct": false},
                    {"answer_id": 627, "text": "Number of leaves", "is_correct": false},
                    {"answer_id": 628, "text": "Length of the longest path from root to a leaf", "is_correct": true}
                ]
            },
            {
                "question_id": 158,
                "text": "Which traversal method visits the root node first?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 629, "text": "Inorder", "is_correct": false},
                    {"answer_id": 630, "text": "Preorder", "is_correct": true},
                    {"answer_id": 631, "text": "Postorder", "is_correct": false},
                    {"answer_id": 632, "text": "Level order", "is_correct": false}
                ]
            },
            {
                "question_id": 159,
                "text": "What defines a balanced tree?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 633, "text": "All levels have the same number of nodes", "is_correct": false},
                    {"answer_id": 634, "text": "Each node has two children", "is_correct": false},
                    {"answer_id": 635, "text": "The height of left and right subtrees of any node differ by at most one", "is_correct": true},
                    {"answer_id": 636, "text": "The tree has no leaf nodes", "is_correct": false}
                ]
            },
            {
                "question_id": 160,
                "text": "What type of tree has nodes with values only greater than the root on the right?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 637, "text": "AVL Tree", "is_correct": false},
                    {"answer_id": 638, "text": "Red-Black Tree", "is_correct": false},
                    {"answer_id": 639, "text": "Binary Search Tree", "is_correct": true},
                    {"answer_id": 640, "text": "Binary Tree", "is_correct": false}
                ]
            },
            {
                "question_id": 161,
                "text": "Which operation on a binary search tree can cause it to become unbalanced?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 641, "text": "Search", "is_correct": false},
                    {"answer_id": 642, "text": "Insertion", "is_correct": true},
                    {"answer_id": 643, "text": "Traversal", "is_correct": false},
                    {"answer_id": 644, "text": "Printing", "is_correct": false}
                ]
            },
            {
                "question_id": 162,
                "text": "What is the time complexity for inserting an element into a binary search tree in the worst case?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 645, "text": "O(n)", "is_correct": true},
                    {"answer_id": 646, "text": "O(log n)", "is_correct": false},
                    {"answer_id": 647, "text": "O(1)", "is_correct": false},
                    {"answer_id": 648, "text": "O(n^2)", "is_correct": false}
                ]
            },
            {
                "question_id": 163,
                "text": "Which case in deletion involves finding the left-most node of the right subtree?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 649, "text": "Deleting a leaf node", "is_correct": false},
                    {"answer_id": 650, "text": "Deleting a node with one child", "is_correct": false},
                    {"answer_id": 651, "text": "Deleting a node with two children", "is_correct": true},
                    {"answer_id": 652, "text": "Deleting the root node", "is_correct": false}
                ]
            },
            {
                "question_id": 164,
                "text": "In a binary search tree, which traversal method is used to get the reverse sorted order of elements?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 653, "text": "Inorder", "is_correct": false},
                    {"answer_id": 654, "text": "Preorder", "is_correct": false},
                    {"answer_id": 655, "text": "Postorder", "is_correct": false},
                    {"answer_id": 656, "text": "Reverse Inorder", "is_correct": true}
                ]
            },
            {
                "question_id": 165,
                "text": "Which tree traversal algorithm is used by search operations in a BST?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 657, "text": "Depth-First Search", "is_correct": true},
                    {"answer_id": 658, "text": "Breadth-First Search", "is_correct": false},
                    {"answer_id": 659, "text": "Binary Search", "is_correct": false},
                    {"answer_id": 660, "text": "Level Order Traversal", "is_correct": false}
                ]
            },
            {
                "question_id": 166,
                "text": "What does the leaf node of a tree signify?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 661, "text": "A node with one child", "is_correct": false},
                    {"answer_id": 662, "text": "A node with two children", "is_correct": false},
                    {"answer_id": 663, "text": "A node with no children", "is_correct": true},
                    {"answer_id": 664, "text": "The root node", "is_correct": false}
                ]
            },
            {
                "question_id": 167,
                "text": "What is a perfectly balanced binary tree?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 665, "text": "A tree where each node has the same number of children", "is_correct": false},
                    {"answer_id": 666, "text": "A tree where all levels are fully filled", "is_correct": true},
                    {"answer_id": 667, "text": "A tree where the height of left and right subtrees of any node differ by at most one", "is_correct": false},
                    {"answer_id": 668, "text": "A tree where all leaf nodes are at the same level", "is_correct": false}
                ]
            },
            {
                "question_id": 168,
                "text": "In a BST, what is the maximum number of children a node can have?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 669, "text": "1", "is_correct": false},
                    {"answer_id": 670, "text": "2", "is_correct": true},
                    {"answer_id": 671, "text": "3", "is_correct": false},
                    {"answer_id": 672, "text": "4", "is_correct": false}
                ]
            },
            {
                "question_id": 169,
                "text": "Which type of tree traversal is best suited for evaluating arithmetic expressions?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 673, "text": "Preorder", "is_correct": false},
                    {"answer_id": 674, "text": "Inorder", "is_correct": false},
                    {"answer_id": 675, "text": "Postorder", "is_correct": true},
                    {"answer_id": 676, "text": "Level Order", "is_correct": false}
                ]
            },
            {
                "question_id": 170,
                "text": "Which of the following is true for a node with two children in a BST?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 677, "text": "A. It can be deleted without reordering", "is_correct": false},
                    {"answer_id": 678, "text": "B. Its in-order predecessor is the maximum value node in its left subtree.", "is_correct": false},
                    {"answer_id": 679, "text": "C. Its in-order successor is the minimum value node in its right subtree", "is_correct": false},
                    {"answer_id": 680, "text": "D. Both B and C are correct", "is_correct": true}
                ]
            },
            {
                "question_id": 171,
                "text": "Which is not a valid property of a binary search tree?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 681, "text": "Left subtree has nodes with values less than the root", "is_correct": false},
                    {"answer_id": 682, "text": "Right subtree has nodes with values greater than the root", "is_correct": false},
                    {"answer_id": 683, "text": "In-order traversal gives nodes in non-decreasing order", "is_correct": false},
                    {"answer_id": 684, "text": "A node with only one child has its child as a leaf node", "is_correct": true}
                ]
            },
            {
                "question_id": 172,
                "text": "What is the primary advantage of using a binary search tree over a linked list?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 685, "text": "Faster deletion", "is_correct": false},
                    {"answer_id": 686, "text": "Easier implementation", "is_correct": false},
                    {"answer_id": 687, "text": "Balanced height", "is_correct": false},
                    {"answer_id": 688, "text": "Faster search", "is_correct": true}
                ]
            },
            {
                "question_id": 173,
                "text": "What is the average-case time complexity for searching in a binary search tree?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 689, "text": "O(n)", "is_correct": false},
                    {"answer_id": 690, "text": "O(log n)", "is_correct": true},
                    {"answer_id": 691, "text": "O(1)", "is_correct": false},
                    {"answer_id": 692, "text": "O(n log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 174,
                "text": "In which scenario does a BST degenerate into a linked list?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 693, "text": "When nodes are inserted in random order", "is_correct": false},
                    {"answer_id": 694, "text": "When nodes are inserted in increasing order", "is_correct": true},
                    {"answer_id": 695, "text": "When nodes are deleted randomly", "is_correct": false},
                    {"answer_id": 696, "text": "When nodes have only one child", "is_correct": false}
                ]
            },
            {
                "question_id": 175,
                "text": "If a BST is traversed in pre-order, which of the following is true?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 697, "text": "Root is visited first", "is_correct": true},
                    {"answer_id": 698, "text": "Leaf nodes are visited first", "is_correct": false},
                    {"answer_id": 699, "text": "Nodes are visited in sorted order", "is_correct": false},
                    {"answer_id": 700, "text": "Nodes are visited level by level", "is_correct": false}
                ]
            },
            {
                "question_id": 176,
                "text": "What is the time complexity of deleting a node with two children in a BST?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 701, "text": "O(n)", "is_correct": false},
                    {"answer_id": 702, "text": "O(log n)", "is_correct": true},
                    {"answer_id": 703, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 704, "text": "O(1)", "is_correct": false}
                ]
            },
            {
                "question_id": 177,
                "text": "What distinguishes a binary search tree from other binary trees?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 705, "text": "Nodes can have up to two children", "is_correct": false},
                    {"answer_id": 706, "text": "It has a root node", "is_correct": false},
                    {"answer_id": 707, "text": "All nodes are connected by edges", "is_correct": false},
                    {"answer_id": 708, "text": "It maintains a sorted order property", "is_correct": true}
                ]
            },
            {
                "question_id": 178,
                "text": "When deleting a node with two children in a BST, which node typically replaces it?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 709, "text": "Left child", "is_correct": false},
                    {"answer_id": 710, "text": "Right child", "is_correct": false},
                    {"answer_id": 711, "text": "In-order predecessor or successor", "is_correct": true},
                    {"answer_id": 712, "text": "Root node", "is_correct": false}
                ]
            },
            {
                "question_id": 179,
                "text": "Which of the following is a characteristic of a balanced binary search tree?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 713, "text": "All leaf nodes are at the same depth", "is_correct": false},
                    {"answer_id": 714, "text": "The height difference between left and right subtrees is no more than one", "is_correct": true},
                    {"answer_id": 715, "text": "It contains only unique values", "is_correct": false},
                    {"answer_id": 716, "text": "It does not have a root node", "is_correct": false}
                ]
            },
            {
                "question_id": 180,
                "text": "How does a BST handle duplicate values?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 717, "text": "Inserts all duplicates in the right subtree", "is_correct": false},
                    {"answer_id": 718, "text": "Inserts all duplicates in the left subtree", "is_correct": false},
                    {"answer_id": 719, "text": "Does not allow duplicates", "is_correct": true},
                    {"answer_id": 720, "text": "Inserts duplicates randomly", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 7,
        "title": "Databases - Conceptual & Logical Design",
        "description": "Test your knowledge on Conceptual & Logical Design!",
        "questions":[        
            {
                "question_id": 181,
                "text": "What is a database?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 721, "text": "A collection of scattered data", "is_correct": false},
                    {"answer_id": 722, "text": "A large collection of persistent data", "is_correct": true},
                    {"answer_id": 723, "text": "A type of application software", "is_correct": false},
                    {"answer_id": 724, "text": "A programming language", "is_correct": false}
                ]
            },
            {
                "question_id": 182,
                "text": "Who invented the concept of relational databases?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 725, "text": "Larry Page", "is_correct": false},
                    {"answer_id": 726, "text": "Bill Gates", "is_correct": false},
                    {"answer_id": 727, "text": "Edgar Codd", "is_correct": true},
                    {"answer_id": 728, "text": "Steve Jobs", "is_correct": false}
                ]
            },
            {
                "question_id": 183,
                "text": "Which of the following is a primary feature of a database?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 729, "text": "Inconsistent data storage", "is_correct": false},
                    {"answer_id": 730, "text": "Accessible from a single application only", "is_correct": false},
                    {"answer_id": 731, "text": "Concurrently accessible and modifiable", "is_correct": true},
                    {"answer_id": 732, "text": "Volatile data storage", "is_correct": false}
                ]
            },
            {
                "question_id": 184,
                "text": "What does ER stand for in ER Diagram?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 733, "text": "Entity-Relation", "is_correct": false},
                    {"answer_id": 734, "text": "Entity-Relationship", "is_correct": true},
                    {"answer_id": 735, "text": "Entity-Resource", "is_correct": false},
                    {"answer_id": 736, "text": "Entity-Retainer", "is_correct": false}
                ]
            },
            {
                "question_id": 185,
                "text": "What symbol is typically used to represent entities in an ER diagram?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 737, "text": "Circle", "is_correct": false},
                    {"answer_id": 738, "text": "Diamond", "is_correct": false},
                    {"answer_id": 739, "text": "Rectangle", "is_correct": true},
                    {"answer_id": 740, "text": "Triangle", "is_correct": false}
                ]
            },
            {
                "question_id": 186,
                "text": "Which SQL command is used to create a table?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 741, "text": "INSERT", "is_correct": false},
                    {"answer_id": 742, "text": "CREATE TABLE", "is_correct": true},
                    {"answer_id": 743, "text": "SELECT", "is_correct": false},
                    {"answer_id": 744, "text": "UPDATE", "is_correct": false}
                ]
            },
            {
                "question_id": 187,
                "text": "What is the primary key in a table?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 745, "text": "A field that can be null", "is_correct": false},
                    {"answer_id": 746, "text": "A field that uniquely identifies each record", "is_correct": true},
                    {"answer_id": 747, "text": "A field that contains duplicate values", "is_correct": false},
                    {"answer_id": 748, "text": "A field that stores primary data", "is_correct": false}
                ]
            },
            {
                "question_id": 188,
                "text": "What does 'VARCHAR' stand for in SQL?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 749, "text": "Variable Character", "is_correct": true},
                    {"answer_id": 750, "text": "Virtual Character", "is_correct": false},
                    {"answer_id": 751, "text": "Verified Character", "is_correct": false},
                    {"answer_id": 752, "text": "Vector Character", "is_correct": false}
                ]
            },
            {
                "question_id": 189,
                "text": "Which command is used to delete a table in SQL?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 753, "text": "REMOVE TABLE", "is_correct": false},
                    {"answer_id": 754, "text": "DELETE TABLE", "is_correct": false},
                    {"answer_id": 755, "text": "DROP TABLE", "is_correct": true},
                    {"answer_id": 756, "text": "CLEAR TABLE", "is_correct": false}
                ]
            },
            {
                "question_id": 190,
                "text": "What is a 'tuple' in a relational database?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 757, "text": "A column", "is_correct": false},
                    {"answer_id": 758, "text": "A row", "is_correct": true},
                    {"answer_id": 759, "text": "A field", "is_correct": false},
                    {"answer_id": 760, "text": "A table", "is_correct": false}
                ]
            },
            {
                "question_id": 191,
                "text": "Which of the following best describes a weak entity?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 761, "text": "An entity that cannot exist without a dependent entity", "is_correct": true},
                    {"answer_id": 762, "text": "An entity that is independent of other entities", "is_correct": false},
                    {"answer_id": 763, "text": "An entity with no attributes", "is_correct": false},
                    {"answer_id": 764, "text": "An entity with multiple primary keys", "is_correct": false}
                ]
            },
            {
                "question_id": 192,
                "text": "In an ER diagram, how are relationships typically represented?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 765, "text": "Circles", "is_correct": false},
                    {"answer_id": 766, "text": "Diamonds", "is_correct": true},
                    {"answer_id": 767, "text": "Rectangles", "is_correct": false},
                    {"answer_id": 768, "text": "Triangles", "is_correct": false}
                ]
            },
            {
                "question_id": 193,
                "text": "What is the purpose of a foreign key in a relational database?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 769, "text": "To uniquely identify records within the table", "is_correct": false},
                    {"answer_id": 770, "text": "To create a link between two tables", "is_correct": true},
                    {"answer_id": 771, "text": "To store foreign language characters", "is_correct": false},
                    {"answer_id": 772, "text": "To improve query performance", "is_correct": false}
                ]
            },
            {
                "question_id": 194,
                "text": "Which of the following is an example of a composite primary key?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 773, "text": "A single column primary key", "is_correct": false},
                    {"answer_id": 774, "text": "A primary key consisting of two or more columns", "is_correct": true},
                    {"answer_id": 775, "text": "A primary key that is auto-incremented", "is_correct": false},
                    {"answer_id": 776, "text": "A primary key that references another table", "is_correct": false}
                ]
            },
            {
                "question_id": 195,
                "text": "In SQL, which clause is used to filter records?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 777, "text": "SELECT", "is_correct": false},
                    {"answer_id": 778, "text": "WHERE", "is_correct": true},
                    {"answer_id": 779, "text": "FROM", "is_correct": false},
                    {"answer_id": 780, "text": "GROUP BY", "is_correct": false}
                ]
            },
            {
                "question_id": 196,
                "text": "What does the 'NOT NULL' constraint ensure in SQL?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 781, "text": "The field must have a default value", "is_correct": false},
                    {"answer_id": 782, "text": "The field cannot have duplicate values", "is_correct": false},
                    {"answer_id": 783, "text": "The field cannot be left empty", "is_correct": true},
                    {"answer_id": 784, "text": "The field must be a primary key", "is_correct": false}
                ]
            },
            {
                "question_id": 197,
                "text": "What is a 'schema' in the context of databases?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 785, "text": "A graphical representation of data", "is_correct": false},
                    {"answer_id": 786, "text": "A logical structure that defines the organisation of data in a database", "is_correct": true},
                    {"answer_id": 787, "text": "A programming language used for databases", "is_correct": false},
                    {"answer_id": 788, "text": "A type of query", "is_correct": false}
                ]
            },
            {
                "question_id": 198,
                "text": "What is the result of the SQL query: SELECT * FROM table_name WHERE condition;?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 789, "text": "It creates a new table", "is_correct": false},
                    {"answer_id": 790, "text": "It inserts new records", "is_correct": false},
                    {"answer_id": 791, "text": "It retrieves records that meet the specified condition", "is_correct": true},
                    {"answer_id": 792, "text": "It deletes records", "is_correct": false}
                ]
            },
            {
                "question_id": 199,
                "text": "Which of the following is an example of a relational database management system (RDBMS)?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 793, "text": "Microsoft Word", "is_correct": false},
                    {"answer_id": 794, "text": "Oracle", "is_correct": true},
                    {"answer_id": 795, "text": "Adobe Photoshop", "is_correct": false},
                    {"answer_id": 796, "text": "Windows OS", "is_correct": false}
                ]
            },
            {
                "question_id": 200,
                "text": "Which of the following is an example of a relational database management system (RDBMS)?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 797, "text": "Adding redundancy to the data", "is_correct": false},
                    {"answer_id": 798, "text": "Structuring data to reduce redundancy and improve integrity", "is_correct": true},
                    {"answer_id": 799, "text": "Increasing the complexity of the databasep", "is_correct": false},
                    {"answer_id": 800, "text": "Simplifying data to make it less secure", "is_correct": false}
                ]
            },
            {
                "question_id": 201,
                "text": "In the context of database design, what is 'referential integrity'?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 801, "text": "Ensuring data is encrypted", "is_correct": false},
                    {"answer_id": 802, "text": "Ensuring that foreign key values in one table correspond to primary key values in another table", "is_correct": true},
                    {"answer_id": 803, "text": "Ensuring all tables have primary keys", "is_correct": false},
                    {"answer_id": 804, "text": "Ensuring all queries are optimised", "is_correct": false}
                ]
            },
            {
                "question_id": 202,
                "text": "Which SQL clause is used to group rows that have the same values in specified columns into summary rows?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 805, "text": "HAVING", "is_correct": false},
                    {"answer_id": 806, "text": "GROUP BY", "is_correct": true},
                    {"answer_id": 807, "text": "ORDER BY", "is_correct": false},
                    {"answer_id": 808, "text": "JOIN", "is_correct": false}
                ]
            },
            {
                "question_id": 203,
                "text": "What does the 'CASCADE' option do when specified in a foreign key constraint?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 809, "text": "Deletes the foreign key constraint", "is_correct": false},
                    {"answer_id": 810, "text": "Deletes the rows in the child table when the corresponding rows in the parent table are deleted", "is_correct": true},
                    {"answer_id": 811, "text": "Prevents deletion of the rows in the parent table", "is_correct": false},
                    {"answer_id": 812, "text": "Updates the rows in the child table when the corresponding rows in the parent table are updated", "is_correct": false}
                ]
            },
            {
                "question_id": 204,
                "text": "In an ER diagram, what does a double rectangle represent?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 813, "text": "A weak entity", "is_correct": true},
                    {"answer_id": 814, "text": "A strong entity", "is_correct": false},
                    {"answer_id": 815, "text": "An attribute", "is_correct": false},
                    {"answer_id": 816, "text": "A relationship", "is_correct": false}
                ]
            },
            {
                "question_id": 205,
                "text": "When designing the schema for a weak entity in a relational database, which of the following is true regarding the primary key?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 817, "text": "The primary key of the weak entity is the same as that of its strong entity", "is_correct": false},
                    {"answer_id": 818, "text": "The primary key of the weak entity only consists of its own attributes", "is_correct": false},
                    {"answer_id": 819, "text": "The primary key of the weak entity includes both the primary key of the strong entity and its own distinguishing attributes", "is_correct": true},
                    {"answer_id": 820, "text": "The weak entity does not have a primary key, relying entirely on the strong entity for identification", "is_correct": false}
                ]
            },
            {
                "question_id": 206,
                "text": "Which SQL statement is used to add a new column to an existing table?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 821, "text": "MODIFY TABLE", "is_correct": false},
                    {"answer_id": 822, "text": "ALTER TABLE", "is_correct": true},
                    {"answer_id": 823, "text": "UPDATE TABLE", "is_correct": false},
                    {"answer_id": 824, "text": "ADD TABLE", "is_correct": false}
                ]
            },
            {
                "question_id": 207,
                "text": "In an ER model, you have a Student entity with two subtypes: Undergraduate and Postgraduate. The Undergraduate and Postgraduate entities are mutually exclusive and together cover all possible Student instances. Which of the following best describes this scenario?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 825, "text": "Partial coverage with overlapping subtypes", "is_correct": false},
                    {"answer_id": 826, "text": "Total coverage with mutually exclusive subtypes", "is_correct": true},
                    {"answer_id": 827, "text": "Total coverage with overlapping subtypes", "is_correct": false},
                    {"answer_id": 828, "text": "Partial coverage with mutually exclusive subtypes", "is_correct": false}
                ]
            },
            {
                "question_id": 208,
                "text": "In a relational database, what is a 'trigger'?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 829, "text": "A command to manually update data", "is_correct": false},
                    {"answer_id": 830, "text": "A rule that automatically performs a specified action when certain conditions are met", "is_correct": true},
                    {"answer_id": 831, "text": "A type of join", "is_correct": false},
                    {"answer_id": 832, "text": "A field that uniquely identifies a record", "is_correct": false}
                ]
            },
            {
                "question_id": 209,
                "text": "Consider a library system where each 'Book' entity can be borrowed by multiple 'Members', but each 'Copy' of a book is unique and can only be borrowed by one 'Member' at a time. What is the correct multiplicity for the borrowed relationship between 'Copy' and 'Member' in the ER diagram?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 833, "text": "(1,1) on both sides", "is_correct": false},
                    {"answer_id": 834, "text": "(0,n) on 'Copy' side and (1,1) on 'Member' side", "is_correct": false},
                    {"answer_id": 835, "text": "(1,n) on 'Copy' side and (0,1) on 'Member' side", "is_correct": false},
                    {"answer_id": 836, "text": "(0,1) on 'Copy' side and (0,n) on 'Member' side", "is_correct": true}
                ]
            },
            {
                "question_id": 210,
                "text": "What is a composite attribute in an ER diagram?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 837, "text": "An attribute that cannot be divided", "is_correct": false},
                    {"answer_id": 838, "text": "An attribute composed of multiple components", "is_correct": true},
                    {"answer_id": 839, "text": "An attribute that serves as a foreign key", "is_correct": false},
                    {"answer_id": 840, "text": "An attribute that serves as a primary key", "is_correct": false}
                ]
            } 
        ]
    },
    {
        "quiz_id": 8,
        "title": "Complexity Analysis, Stacks, Queues and Heaps",
        "description": "Test your knowledge on Complexity Analysis, Stacks, Queues and Heaps!",
        "questions":[    
            {
                "question_id": 211,
                "text": "What principle does a stack follow?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 841, "text": "First-In-First-Out (FIFO)", "is_correct": false},
                    {"answer_id": 842, "text": "Last-In-First-Out (LIFO)", "is_correct": true},
                    {"answer_id": 843, "text": "Last-In-First-In (LIFI)", "is_correct": false},
                    {"answer_id": 844, "text": "First-In-Last-Out (FILO)", "is_correct": false}
                ]
            },
            {
                "question_id": 212,
                "text": "Which of the following operations is used to remove the top element of a stack?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 845, "text": "push", "is_correct": false},
                    {"answer_id": 846, "text": "pop", "is_correct": true},
                    {"answer_id": 847, "text": "enqueue", "is_correct": false},
                    {"answer_id": 848, "text": "dequeue", "is_correct": false}
                ]
            },
            {
                "question_id": 213,
                "text": "In a queue, where is the new element inserted?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 849, "text": "Front", "is_correct": false},
                    {"answer_id": 850, "text": "Rear", "is_correct": true},
                    {"answer_id": 851, "text": "Middle", "is_correct": false},
                    {"answer_id": 852, "text": "Random position", "is_correct": false}
                ]
            },
            {
                "question_id": 214,
                "text": "What is the time complexity of the push operation in a stack implemented using an array?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 853, "text": "O(n)", "is_correct": false},
                    {"answer_id": 854, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 855, "text": "O(1)", "is_correct": true},
                    {"answer_id": 856, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 215,
                "text": "Which data structure uses the First-In-First-Out (FIFO) principle?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 857, "text": "Stack", "is_correct": false},
                    {"answer_id": 858, "text": "Queue", "is_correct": true},
                    {"answer_id": 859, "text": "Array", "is_correct": false},
                    {"answer_id": 860, "text": "Linked list", "is_correct": false}
                ]
            },
            {
                "question_id": 216,
                "text": "What is the time complexity of the dequeue operation in a queue implemented using an array?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 861, "text": "O(n)", "is_correct": false},
                    {"answer_id": 862, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 863, "text": "O(1)", "is_correct": true},
                    {"answer_id": 864, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 217,
                "text": "In a max-heap, where is the largest element found?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 865, "text": "At the root", "is_correct": true},
                    {"answer_id": 866, "text": "At the leftmost leaf", "is_correct": false},
                    {"answer_id": 867, "text": "At the rightmost leaf", "is_correct": false},
                    {"answer_id": 868, "text": "Anywhere in the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 218,
                "text": "What does the heap property ensure in a max-heap?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 869, "text": "Parent node is always smaller than its children", "is_correct": false},
                    {"answer_id": 870, "text": "Parent node is always greater than its children", "is_correct": true},
                    {"answer_id": 871, "text": "All nodes are equal", "is_correct": false},
                    {"answer_id": 872, "text": "All leaves are at the same level", "is_correct": false}
                ]
            },
            {
                "question_id": 219,
                "text": "What is the time complexity of the Max-Heapify operation?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 873, "text": "O(n)", "is_correct": false},
                    {"answer_id": 874, "text": "O(log n)", "is_correct": true},
                    {"answer_id": 875, "text": "O(1)", "is_correct": false},
                    {"answer_id": 876, "text": "O(n log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 220,
                "text": "Which sorting algorithm uses a binary heap?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 877, "text": "Quick Sort", "is_correct": false},
                    {"answer_id": 878, "text": "Merge Sort", "is_correct": false},
                    {"answer_id": 879, "text": "Bubble Sort", "is_correct": false},
                    {"answer_id": 880, "text": "Heap Sort", "is_correct": true}
                ]
            },
            {
                "question_id": 221,
                "text": "What happens when you try to pop from an empty stack?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 881, "text": "It returns a null value", "is_correct": false},
                    {"answer_id": 882, "text": "It throws an overflow error", "is_correct": false},
                    {"answer_id": 883, "text": "It throws an underflow error", "is_correct": true},
                    {"answer_id": 884, "text": "It adds a new element to the stack", "is_correct": false}
                ]
            },
            {
                "question_id": 222,
                "text": "In an array-based implementation of a queue, what formula is used to calculate the position of the tail after an enqueue operation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 885, "text": "(tail + 1) % size", "is_correct": true},
                    {"answer_id": 886, "text": "(tail + size) % size", "is_correct": false},
                    {"answer_id": 887, "text": "(tail - 1) % size", "is_correct": false},
                    {"answer_id": 888, "text": "(tail * 2) % size", "is_correct": false}
                ]
            },
            {
                "question_id": 223,
                "text": "What is the time complexity of inserting an element into a max-heap?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 889, "text": "O(n)", "is_correct": false},
                    {"answer_id": 890, "text": "O(log n)", "is_correct": true},
                    {"answer_id": 891, "text": "O(1)", "is_correct": false},
                    {"answer_id": 892, "text": "O(n log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 224,
                "text": "During the insertion sort, what is the worst-case time complexity?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 893, "text": "O(n)", "is_correct": false},
                    {"answer_id": 894, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 895, "text": "O(n^2)", "is_correct": true},
                    {"answer_id": 896, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 225,
                "text": "Which data structure is best suited for implementing recursion?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 897, "text": "Queue", "is_correct": false},
                    {"answer_id": 898, "text": "Stack", "is_correct": true},
                    {"answer_id": 899, "text": "Heap", "is_correct": false},
                    {"answer_id": 900, "text": "Graph", "is_correct": false}
                ]
            },
            {
                "question_id": 226,
                "text": "In a circular queue, what happens when the head and tail pointers are equal?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 901, "text": "The queue is empty", "is_correct": true},
                    {"answer_id": 902, "text": "The queue is full", "is_correct": false},
                    {"answer_id": 903, "text": "The queue is half full", "is_correct": false},
                    {"answer_id": 904, "text": "The queue is in an invalid state", "is_correct": false}
                ]
            },
            {
                "question_id": 227,
                "text": "What is the height of a complete binary tree with n nodes?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 905, "text": "log2(n)", "is_correct": true},
                    {"answer_id": 906, "text": "n", "is_correct": false},
                    {"answer_id": 907, "text": "nlog2(n)", "is_correct": false},
                    {"answer_id": 908, "text": "log2 (n+1)", "is_correct": false}
                ]
            },
            {
                "question_id": 228,
                "text": "What does the ‘enqueue’ operation do in a queue?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 909, "text": "Removes an element from the front", "is_correct": false},
                    {"answer_id": 910, "text": "Adds an element to the rear", "is_correct": true},
                    {"answer_id": 911, "text": "Checks if the queue is full", "is_correct": false},
                    {"answer_id": 912, "text": "Checks if the queue is empty", "is_correct": false}
                ]
            },
            {
                "question_id": 229,
                "text": "In the context of heaps, what is the 'heapify' operation?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 913, "text": "Adding an element to the heap", "is_correct": false},
                    {"answer_id": 914, "text": "Removing the root of the heap", "is_correct": false},
                    {"answer_id": 915, "text": "Adjusting the heap to maintain the heap property", "is_correct": true},
                    {"answer_id": 916, "text": "Sorting the elements in the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 230,
                "text": "Which operation in heapsort involves repeatedly extracting the maximum element?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 917, "text": "Insertion", "is_correct": false},
                    {"answer_id": 918, "text": "Heapify", "is_correct": false},
                    {"answer_id": 919, "text": "Max-Heapify", "is_correct": false},
                    {"answer_id": 920, "text": "Extract-Max", "is_correct": true}
                ]
            },
            {
                "question_id": 231,
                "text": "In a stack, how can you implement a minimum function to return the minimum element in constant time?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 921, "text": "Use an additional stack to keep track of minimum values", "is_correct": true},
                    {"answer_id": 922, "text": "Use a variable to keep track of the minimum value", "is_correct": false},
                    {"answer_id": 923, "text": "Use a queue to track the minimum values", "is_correct": false},
                    {"answer_id": 924, "text": "Use a linked list to store the minimum values", "is_correct": false}
                ]
            },
            {
                "question_id": 232,
                "text": "What is the amortized time complexity of enqueue and dequeue operations in a dynamic array-based queue implementation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 925, "text": "O(n)", "is_correct": false},
                    {"answer_id": 926, "text": "O(log n)", "is_correct": false},
                    {"answer_id": 927, "text": "O(1)", "is_correct": true},
                    {"answer_id": 928, "text": "O(n^2)", "is_correct": false}
                ]
            },
            {
                "question_id": 233,
                "text": "In heapsort, what is the time complexity of building a max-heap from an unsorted array of n elements?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 929, "text": "O(n log n)", "is_correct": true},
                    {"answer_id": 930, "text": "O(n)", "is_correct": false},
                    {"answer_id": 931, "text": "O(n^2)", "is_correct": false},
                    {"answer_id": 932, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 234,
                "text": "What is the key difference between a priority queue and a regular queue?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 933, "text": "Elements are sorted by their values", "is_correct": true},
                    {"answer_id": 934, "text": "Elements are processed in the order they arrive", "is_correct": false},
                    {"answer_id": 935, "text": "Only the largest element can be dequeued", "is_correct": false},
                    {"answer_id": 936, "text": "Only the smallest element can be dequeued", "is_correct": false}
                ]
            },
            {
                "question_id": 235,
                "text": "In the context of heaps, what is the extract-max operation?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 937, "text": "It removes and returns the root of a max-heap", "is_correct": true},
                    {"answer_id": 938, "text": "It adds a new element to the heap", "is_correct": false},
                    {"answer_id": 939, "text": "It finds the maximum element without removing it", "is_correct": false},
                    {"answer_id": 940, "text": "It restructures the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 236,
                "text": "Why does heapsort have a better worst-case time complexity compared to quicksort?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 941, "text": "It does not involve recursion", "is_correct": false},
                    {"answer_id": 942, "text": "It uses a binary tree structure", "is_correct": false},
                    {"answer_id": 943, "text": "It always divides the input in half", "is_correct": false},
                    {"answer_id": 944, "text": "It does not depend on the choice of pivot", "is_correct": true}
                ]
            },
            {
                "question_id": 237,
                "text": "What is the purpose of the 'build-max-heap' function in heapsort?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 945, "text": "To sort the elements in ascending order", "is_correct": false},
                    {"answer_id": 946, "text": "To convert an unsorted array into a max-heap", "is_correct": true},
                    {"answer_id": 947, "text": "To find the maximum element in the array", "is_correct": false},
                    {"answer_id": 948, "text": "To insert a new element into the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 238,
                "text": "Which data structure can be used to implement both stack and queue operations efficiently?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 949, "text": "Array", "is_correct": false},
                    {"answer_id": 950, "text": "Linked list", "is_correct": true},
                    {"answer_id": 951, "text": "Heap", "is_correct": false},
                    {"answer_id": 952, "text": "Graph", "is_correct": false}
                ]
            },
            {
                "question_id": 239,
                "text": "What is the purpose of the 'decrease-key' operation in a heap?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 953, "text": "To increase the value of a node", "is_correct": false},
                    {"answer_id": 954, "text": "To decrease the value of a node", "is_correct": true},
                    {"answer_id": 955, "text": "To remove a node from the heap", "is_correct": false},
                    {"answer_id": 956, "text": "To find the minimum value in the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 240,
                "text": "In a min-heap, how do you ensure the minimum element is always at the root?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 957, "text": "By maintaining the heap property during insertion and deletion", "is_correct": true},
                    {"answer_id": 958, "text": "By sorting the elements after each insertion", "is_correct": false},
                    {"answer_id": 959, "text": "By performing a level-order traversal after each deletion", "is_correct": false},
                    {"answer_id": 960, "text": "By using an additional array to track the minimum element", "is_correct": false}
                ]
            }
        ]
    },
    {
        "quiz_id": 9,
        "title": "Sorting and Hash tables",
        "description": "Test your knowledge on Sorting and Hash tables!",
        "questions":[    
            {
                "question_id": 241,
                "text": "What is the main characteristic of insertion sort?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 961, "text": "It uses a binary tree", "is_correct": false},
                    {"answer_id": 962, "text": "It uses the divide-and-conquer method", "is_correct": false},
                    {"answer_id": 963, "text": "It is simple and intuitive", "is_correct": true},
                    {"answer_id": 964, "text": "It requires a heap", "is_correct": false}
                ]
            },
            {
                "question_id": 242,
                "text": "Which sorting algorithm is based on the divide-and-conquer method?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 965, "text": "Insertion Sort", "is_correct": false},
                    {"answer_id": 966, "text": "Bubble Sort", "is_correct": false},
                    {"answer_id": 967, "text": "Merge Sort", "is_correct": true},
                    {"answer_id": 968, "text": "Selection Sort", "is_correct": false}
                ]
            },
            {
                "question_id": 243,
                "text": "In a max-heap, where is the largest element stored?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 969, "text": "At any leaf node", "is_correct": false},
                    {"answer_id": 970, "text": "At the root node", "is_correct": true},
                    {"answer_id": 971, "text": "In the middle of the array", "is_correct": false},
                    {"answer_id": 972, "text": "At the last node", "is_correct": false}
                ]
            },
            {
                "question_id": 244,
                "text": "What is the time complexity of insertion sort in the worst case?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 973, "text": "O(n)", "is_correct": false},
                    {"answer_id": 974, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 975, "text": "O(n^2)", "is_correct": true},
                    {"answer_id": 976, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 245,
                "text": "Which operation does not belong to heapsort?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 977, "text": "Heapify", "is_correct": false},
                    {"answer_id": 978, "text": "Extract-Max", "is_correct": false},
                    {"answer_id": 979, "text": "Insertion", "is_correct": false},
                    {"answer_id": 980, "text": "Merge", "is_correct": true}
                ]
            },
            {
                "question_id": 246,
                "text": "What does the 'heapify' operation do in a heap?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 981, "text": "Removes the root element", "is_correct": false},
                    {"answer_id": 982, "text": "Adds a new element to the heap", "is_correct": false},
                    {"answer_id": 983, "text": "Maintains the heap property", "is_correct": true},
                    {"answer_id": 984, "text": "Sorts the elements in the heap", "is_correct": false}
                ]
            },
            {
                "question_id": 247,
                "text": "What is the main advantage of heapsort?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 985, "text": "It is simple and intuitive", "is_correct": false},
                    {"answer_id": 986, "text": "It works well with linked lists", "is_correct": false},
                    {"answer_id": 987, "text": "It has O(n log n) time complexity", "is_correct": true},
                    {"answer_id": 988, "text": "It is stable", "is_correct": false}
                ]
            },
            {
                "question_id": 248,
                "text": "In a hash table, what is a 'bucket'?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 989, "text": "A storage device", "is_correct": false},
                    {"answer_id": 990, "text": "A linked list used to handle collisions", "is_correct": true},
                    {"answer_id": 991, "text": "An element of the hash table", "is_correct": false},
                    {"answer_id": 992, "text": "A type of sorting algorithm", "is_correct": false}
                ]
            },
            {
                "question_id": 249,
                "text": "What is the primary purpose of a hash function?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 993, "text": "To sort data", "is_correct": false},
                    {"answer_id": 994, "text": "To compress data", "is_correct": false},
                    {"answer_id": 995, "text": "To map data to fixed-size values", "is_correct": true},
                    {"answer_id": 996, "text": "To encrypt data", "is_correct": false}
                ]
            },
            {
                "question_id": 250,
                "text": "Which sorting algorithm is considered inefficient for large datasets but performs well on small datasets?",
                "difficulty_level": 1,
                "answers": [
                    {"answer_id": 997, "text": "Quick Sort", "is_correct": false},
                    {"answer_id": 998, "text": "Merge Sort", "is_correct": false},
                    {"answer_id": 999, "text": "Insertion Sort", "is_correct": true},
                    {"answer_id": 1000, "text": "Heapsort", "is_correct": false}
                ]
            },
            {
                "question_id": 251,
                "text": "Which of the following steps is NOT part of the heapsort algorithm?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1001, "text": "Build-Max-Heap", "is_correct": false},
                    {"answer_id": 1002, "text": "Merge subarrays", "is_correct": true},
                    {"answer_id": 1003, "text": "Swap the root with the last element", "is_correct": false},
                    {"answer_id": 1004, "text": "Reduce the heap size", "is_correct": false}
                ]
            },
            {
                "question_id": 252,
                "text": "In merge sort, what happens during the merging phase?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1005, "text": "The array is divided into smaller subarrays", "is_correct": false},
                    {"answer_id": 1006, "text": "The subarrays are combined into a sorted array", "is_correct": true},
                    {"answer_id": 1007, "text": "The largest element is placed at the end", "is_correct": false},
                    {"answer_id": 1008, "text": "Elements are shifted to their correct positions", "is_correct": false}
                ]
            },
            {
                "question_id": 253,
                "text": "What is the time complexity of heapsort in the worst case?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1009, "text": "O(n)", "is_correct": false},
                    {"answer_id": 1010, "text": "O(n log n)", "is_correct": true},
                    {"answer_id": 1011, "text": "O(n^2)", "is_correct": false},
                    {"answer_id": 1012, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 254,
                "text": "In quicksort, what is the purpose of the pivot element?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1013, "text": "To find the median of the array", "is_correct": false},
                    {"answer_id": 1014, "text": "To divide the array into two subarrays", "is_correct": true},
                    {"answer_id": 1015, "text": "To merge sorted arrays", "is_correct": false},
                    {"answer_id": 1016, "text": "To heapify the array", "is_correct": false}
                ]
            },
            {
                "question_id": 255,
                "text": "What is the key disadvantage of using a simple hash function?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1017, "text": "It is too slow", "is_correct": false},
                    {"answer_id": 1018, "text": "It cannot handle large datasets", "is_correct": false},
                    {"answer_id": 1019, "text": "It can cause many collisions", "is_correct": true},
                    {"answer_id": 1020, "text": "It requires sorting of elements", "is_correct": false}
                ]
            },
            {
                "question_id": 256,
                "text": "In a hash table, what happens when a collision occurs?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1021, "text": "The data is discarded", "is_correct": false},
                    {"answer_id": 1022, "text": "The data is rehashed", "is_correct": false},
                    {"answer_id": 1023, "text": "A collision resolution strategy is used", "is_correct": true},
                    {"answer_id": 1024, "text": "The table size is doubled", "is_correct": false}
                ]
            },
            {
                "question_id": 257,
                "text": "Which of the following is a collision resolution strategy in hash tables?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1025, "text": "Merging", "is_correct": false},
                    {"answer_id": 1026, "text": "Chaining", "is_correct": true},
                    {"answer_id": 1027, "text": "Sorting", "is_correct": false},
                    {"answer_id": 1028, "text": "Heapifying", "is_correct": false}
                ]
            },
            {
                "question_id": 258,
                "text": "What is the purpose of the 'Extract-Max' operation in a max-heap?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1029, "text": "To remove and return the largest element", "is_correct": true},
                    {"answer_id": 1030, "text": "To add a new element to the heap", "is_correct": false},
                    {"answer_id": 1031, "text": "To sort the heap", "is_correct": false},
                    {"answer_id": 1032, "text": "To decrease the key of the root", "is_correct": false}
                ]
            },
            {
                "question_id": 259,
                "text": "What is the main advantage of using quicksort over other sorting algorithms?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1033, "text": "It is stable", "is_correct": false},
                    {"answer_id": 1034, "text": "It has a guaranteed O(n log n) time complexity", "is_correct": false},
                    {"answer_id": 1035, "text": "It has a small constant factor and is usually faster in practice", "is_correct": true},
                    {"answer_id": 1036, "text": "It uses additional memory for merging", "is_correct": false}
                ]
            },
            {
                "question_id": 260,
                "text": "Which of the following best describes a 'load factor' in a hash table?",
                "difficulty_level": 2,
                "answers": [
                    {"answer_id": 1037, "text": "The number of elements in the table", "is_correct": false},
                    {"answer_id": 1038, "text": "The size of the table", "is_correct": false},
                    {"answer_id": 1039, "text": "The ratio of the number of elements to the table size", "is_correct": true},
                    {"answer_id": 1040, "text": "The time complexity of hash function", "is_correct": false}
                ]
            },
            {
                "question_id": 261,
                "text": "What is the time complexity of quicksort in the worst case?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1041, "text": "O(n)", "is_correct": false},
                    {"answer_id": 1042, "text": "O(n log n)", "is_correct": false},
                    {"answer_id": 1043, "text": "O(n^2)", "is_correct": true},
                    {"answer_id": 1044, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 262,
                "text": "Why is merge sort preferred for sorting linked lists over arrays?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1045, "text": "It has a lower time complexity", "is_correct": false},
                    {"answer_id": 1046, "text": "It does not require additional space", "is_correct": false},
                    {"answer_id": 1047, "text": "It performs well with sequential access", "is_correct": true},
                    {"answer_id": 1048, "text": "It is a stable sorting algorithm", "is_correct": false}
                ]
            },
            {
                "question_id": 263,
                "text": "Which sorting algorithm is NOT stable?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1049, "text": "Merge Sort", "is_correct": false},
                    {"answer_id": 1050, "text": "Insertion Sort", "is_correct": false},
                    {"answer_id": 1051, "text": "Quick Sort", "is_correct": true},
                    {"answer_id": 1052, "text": "Bubble Sort", "is_correct": false}
                ]
            },
            {
                "question_id": 264,
                "text": "What is the average-case time complexity of quicksort?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1053, "text": "O(n)", "is_correct": false},
                    {"answer_id": 1054, "text": "O(n log n)", "is_correct": true},
                    {"answer_id": 1055, "text": "O(n^2)", "is_correct": false},
                    {"answer_id": 1056, "text": "O(log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 265,
                "text": "In a hash table with chaining, what is the expected time complexity for search operations?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1057, "text": "O(1)", "is_correct": true},
                    {"answer_id": 1058, "text": "O(log n)", "is_correct": false},
                    {"answer_id": 1059, "text": "O(n)", "is_correct": false},
                    {"answer_id": 1060, "text": "O(n log n)", "is_correct": false}
                ]
            },
            {
                "question_id": 266,
                "text": "What is the main disadvantage of merge sort despite its efficiency?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1061, "text": "It is not stable", "is_correct": false},
                    {"answer_id": 1062, "text": "It has a high time complexity", "is_correct": false},
                    {"answer_id": 1063, "text": "It requires additional memory proportional to the size of the input array", "is_correct": true},
                    {"answer_id": 1064, "text": "It performs poorly on small datasets", "is_correct": false}
                ]
            },
            {
                "question_id": 267,
                "text": "Which operation is the most time-consuming in the process of heapsort?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1065, "text": "Build-Max-Heap", "is_correct": true},
                    {"answer_id": 1066, "text": "Heapify", "is_correct": true},
                    {"answer_id": 1067, "text": "Swap", "is_correct": false},
                    {"answer_id": 1068, "text": "Extract-Max", "is_correct": false}
                ]
            },
            {
                "question_id": 268,
                "text": "How does quicksort handle elements equal to the pivot?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1069, "text": "Places them all in the left subarray", "is_correct": false},
                    {"answer_id": 1070, "text": "Places them all in the right subarray", "is_correct": false},
                    {"answer_id": 1071, "text": "Leaves them in their original positions", "is_correct": false},
                    {"answer_id": 1072, "text": "It depends on the implementation", "is_correct": true}
                ]
            },
            {
                "question_id": 269,
                "text": "What is the main purpose of rehashing in a hash table?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1073, "text": "To reduce the load factor", "is_correct": true},
                    {"answer_id": 1074, "text": "To increase the load factor", "is_correct": false},
                    {"answer_id": 1075, "text": "To merge buckets", "is_correct": false},
                    {"answer_id": 1076, "text": "To sort the elements", "is_correct": false}
                ]
            },
            {
                "question_id": 270,
                "text": "What is the main advantage of using double hashing over linear probing in hash tables?",
                "difficulty_level": 3,
                "answers": [
                    {"answer_id": 1077, "text": "It requires less memory", "is_correct": false},
                    {"answer_id": 1078, "text": "It reduces the likelihood of primary clustering", "is_correct": true},
                    {"answer_id": 1079, "text": "It is easier to implement", "is_correct": false},
                    {"answer_id": 1080, "text": "It has a lower time complexity", "is_correct": false}
                ]
            }
        ]
    }
]

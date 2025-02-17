def generator_function():
    try:
        print("Entering try block")
        yield "Yielding from generator"
    finally:
        print("Executing finally block")

def calling_function():
    gen = generator_function()
    try:
        value = next(gen)  # Calling the generator function
        print(f"Received: {value}")
    except StopIteration:
        print("Generator finished")
    finally:
        print("Calling function cleanup")

# Running the function
# calling_function()



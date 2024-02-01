# {{Person}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```
As a Person
So that I can keep my items safe
I want to be able to store items in my backpack.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE
class Person():
    def __init__(self):
        self.backpack = []


    def add_item_to_backpack(self, item):
        """It takes a string, and stores it in the backpack.

        Parameters: (list all parameters and their types)
            item: a string, a word, describing the item (e.g. "book")

        Returns: (state the return value and its type)
            Nothing (None)

        Side effects: (state any side effects)
            It adds the item into the self.backpack
        """
        pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a Person object is instantiated
It intantiates with an empty list.
"""
person = Person()

actual = person.backpack
expected = []

assert actual == expected


"""
Given a Person puts a book in their backpack
The backpack will contain the book.
"""
person = Person()
person.add_items_to_backpack("book")

actual = person.backpack
expected = ["book"]

assert actual == expected

"""
Given a Person puts empty string in their backpack
An Exception is thrown
"""
person = Person()
with pytest.raises(Exception) as e:
    person.add_item_to_backpack("")

actual = str(e.value)
expected = "Please provide an item to put in the backpack!"

assert actual == expected
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE



```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

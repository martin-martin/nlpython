# Problem: Try to cap elements in the list correctly.

hiking = ["devil's den",
            "old lady",
            "north rim",
            "where angel's fly",
            "martin's trail",
            "casey's swimlane"]

# Submitted solution
hiking_string = ", ".join(hiking)
capped_hiking = hiking_string.title()
# assign the output to a variable in order to use it later on
# in this case I simply re-assign it to the same variable name
capped_hiking = capped_hiking.replace('S', 's')
# as 'capped_hiking' is now a *string*, we need to turn it back into a list
c_hiking = capped_hiking.split(',')
# due to the transformations, we have *unnecessary white spaces*
for t in c_hiking:
    print(t.lstrip())  # lstrip() removes space chars from the left side

# adding "casey's swimlane" to the trail list clarifies why this is not
# a generalized good solution: any big 'S' will be converted to lowercase
# but we only want to counteract an issue that comes from *apostrophes*
# therefore, it is better to address them instead of the 'S's

# NOTE: we could continue fixing yet another piece of the code and
# introducing a remedy for the 'S' issue. However, *nearly always* it is
# better to re-think your approach and figure out an easier and cleaner
# solution - even if that means abandoning the path you chose first.

print()  # empty line to separate the solutions visually

# ---------------------------------------------------------------
# Option Nr. 2 - explicitly addressing apostrophes
# ---------------------------------------------------------------
apostrophe = "'"
for trail in hiking:
    trail = trail.title()
    # looking for a general catch statement addressing the '
    # (defining 'apostrophe' as a variable makes the code more readable here)
    if apostrophe in trail:
        # if it's in there, lowercase the incorrectly capitalized 'S'
        # note that the ' is part of the search term to avoid
        # lowercasing words that start with an 'S'
        trail = trail.replace("'S", "'s")
    print(trail)

# NOTE: the above is still a 'hacky' solution, because it only handles
# posessives. Any other apostrophe in a word (e.g. "you're") would still
# break the expected functionality.

print()  # empty line to separate the solutions visually

# ---------------------------------------------------------------
# Option Nr. 3 - (often the easiest!!) Using a package
# ---------------------------------------------------------------
import string

for trail in hiking:
    print(string.capwords(trail))

# simple and elegant - and works! Google search for the win!

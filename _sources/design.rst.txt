design
======

.. button-link:: https://sphinx-design.readthedocs.io/en/latest/

:octicon:`link;2em;sd-text-info`



:octicon:`link;1em;sd-text-info` https://sphinx-design.readthedocs.io/en/latest/

.. button-link:: https://sphinx-design.readthedocs.io/en/latest/

    desgin link
    :octicon:`link;1em;sd-text-info`

.. grid:: 1 2 3 4
    :outline:

    .. grid-item::

        A

    .. grid-item::

        B

    .. grid-item::

        C

    .. grid-item::

        D

.. card:: Card Title

    Card content
    
.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer
    
    
.. grid:: 2

    .. grid-item-card::  Title 1

        A

    .. grid-item-card::  Title 2

        B
        
.. _cards-clickable:

Cards Clickable
...............

.. card:: Clickable Card (external)
    :link: https://example.com

    The entire card can be clicked to navigate to https://example.com.

.. card:: Clickable Card (internal)
    :link: cards-clickable
    :link-type: ref

    The entire card can be clicked to navigate to the ``cards`` reference target.
    
.. dropdown::

    Dropdown content

.. dropdown:: Dropdown title

    Dropdown content

.. dropdown:: Open dropdown
    :open:

    Dropdown content
    
:bdg:`plain badge`

:bdg-primary:`primary`, :bdg-primary-line:`primary-line`

:bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`

:bdg-success:`success`, :bdg-success-line:`success-line`

:bdg-info:`info`, :bdg-info-line:`info-line`

:bdg-warning:`warning`, :bdg-warning-line:`warning-line`

:bdg-danger:`danger`, :bdg-danger-line:`danger-line`

:bdg-light:`light`, :bdg-light-line:`light-line`

:bdg-dark:`dark`, :bdg-dark-line:`dark-line`

:bdg-link-primary:`https://example.com`

:bdg-link-primary-line:`explicit title <https://example.com>`


.. button-link:: https://example.com

.. button-link:: https://example.com

    Button text

.. button-link:: https://example.com
    :color: primary
    :shadow:

.. button-link:: https://example.com
    :color: primary
    :outline:

.. button-link:: https://example.com
    :color: secondary
    :expand:
    
A coloured icon: :octicon:`report;1em;sd-text-info`, some more text.
A coloured icon: :octicon:`link;4em;sd-text-info`, some more text.

- A regular icon: :material-regular:`data_exploration;2em`, some more text
- A coloured regular icon: :material-regular:`settings;3em;sd-text-success`, some more text.
- A coloured outline icon: :material-outlined:`settings;3em;sd-text-success`, some more text.
- A coloured sharp icon: :material-sharp:`settings;3em;sd-text-success`, some more text.
- A coloured round icon: :material-round:`settings;3em;sd-text-success`, some more text.
- A coloured two-tone icon: :material-twotone:`settings;3em;sd-text-success`, some more text.
- A fixed size icon: :material-regular:`data_exploration;24px`, some more text.


- An icon :fas:`spinner;sd-text-primary`, some more text.
- An icon :fab:`github`, some more text.
- An icon :fab:`gitkraken;sd-text-success fa-xl`, some more text.
- An icon :fas:`skull;sd-text-danger`, some more text.


.. article-info::
    :avatar: ../images/ebp-logo.webp
    :avatar-link: https://executablebooks.org/
    :avatar-outline: muted
    :author: Executable Books
    :date: Jul 24, 2021
    :read-time: 5 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1
    
.. button-link:: https://example.com :octicon:`link;2em;sd-text-info`, some more text.

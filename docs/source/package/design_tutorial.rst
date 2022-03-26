.. General Design Tutorial:

**********************************
Aguaclara Package: Design Tutorial
**********************************

Import Aguaclara package and any sub-packages
=====================================================================

Typically when using the Aguaclara Package to design will require the use of units.
Below is an example of importing the package and importing the sub-package units.

.. code-block:: python

    import aguaclara as ac 
    from aguaclara.core.units import u

Now that we have imported the appropriate libraries lets use the Aguaclara package and the units package to 
implement a water treatment plant.

.. code-block:: python

    # Design a water treatment plant
    plant = ac.Plant(
    q = 40 * u.L / u.s,
    cdc = ac.CDC(coag_type = 'pacl'),
    floc = ac.Flocculator(hl = 40 * u.cm),
    sed = ac.Sedimentor(temp = 20 * u.degC),
    filter = ac.Filter(q = 20 * u.L / u.s)
    )

At this point you may be wondering how I knew how to build the plant. The answer is in the 
Aguaclara documentation: `Component Documentaton <https://aguaclara.github.io/aguaclara/design/component.html>`_ 
As you glance over the documentation you may notice ``**kwargs`` and be confused. This argument just means that 
you can specify multiple arguments that were not in the most basic plant specification. Adding more arguments just 
means you are providing more information on what your plant should have such as cdc,floc,sed and filter.

---------------------------------------------------
Using Your Design To Get Other Relevant Information
---------------------------------------------------

Using the design that you create above you can use methods associated with that object(design) to obtain the information
on the plant that you create almost instantly. For instance if we want the properties of plants without tracing through all
of the inputs and obtaining them manually then we can use 

.. code-block:: python

    # This is a method that comes with the component class and invoking it gives the sub-components or subclasses of this given classes the same
    # attributes as the plant
    plant.set_subcomponents()

---------
Exercises
---------

1. Using the documentation in the aguaclara package design an entrance tank with a flow rate of 30 L/s and a flocculator channel depth of 43 inches.
2. Using the documentation in the aguaclara package design a sedimentation tank with a flow rate of 30L/s, set the temperature for the channel to be 20 degrees celsius and a wall thickness of your choice.
3. Choosing one of the above designs utilize a method from either of them.





    
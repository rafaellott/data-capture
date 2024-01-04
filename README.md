# Python Tech Challenge

## How to install?

With a open terminal, go to folder with `cd` and then execute
the pip install command: `$ pip install .`

This will install the library name `datadata_capture`

## How to use?

After successfully install the library, you can use it like:

    from data_capture.main import DataCapture
    
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    
    stats = capture.build_stats()
    stats.less(4)
    stats.between(3, 6)
    stats.greater(4)

    # The less and greater can also be uses like
    stats < 4
    stats > 4
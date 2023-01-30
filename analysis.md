- courses: 
    - name 
    - image
    - lang
    - price
    - created at
    - requerments
    - about
    - studients count


    - content ( relation: one_to_one ):
        - name
        - tests
        - file-pdfs
        - videos


    - instructor ( relation: foreognkey ):
        - name
        - email
        - studients count
        - rate
        - about

    

    - reviews ( relation : foreognkey):
        - user
        - review
        - created at
        - rate
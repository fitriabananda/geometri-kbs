;Start CLIPS
(deftemplate segitiga "atribut segitiga"
            (slot jenis)
            (slot sisi)
            (slot sudut)
            (multislot jenissudut)
            (multislot panjangsisi)
            (slot kesamaansudut)
            (slot kesamaansisi)
)

(deftemplate segiempat "atribut segiempat"
            (slot jenis)
            (slot sisi)
            (slot sudut)
            (multislot jenissudut)
            (multislot panjangsisi)
            (slot kesamaansudut)
            (slot kesamaansisi)
            (slot sisisejajar)
)

(deftemplate segilima "atribut segilima"
            (slot jenis)
            (slot sisi)
            (slot sudut)
            (multislot jenissudut)
            (multislot panjangsisi)
)

(deftemplate segienam "atribut segienam"
            (slot jenis)
            (slot sisi)
            (slot sudut)
            (multislot jenissudut)
            (multislot panjangsisi)
)

(deffacts shape_rules "bentuk"
    (segitiga (sisi 3) (sudut 3))
    (segiempat (sisi 4) (sudut 4))
    (segilima (sisi 5) (sudut 5))
    (segienam (sisi 6) (sudut 6))
)


(defrule is-segitiga
    (sisi 3)
    (sudut 3)
=> 
    (assert (shape-is segitiga)))

(defrule is-segiempat
    (sisi 4)
    (sudut 4)
=> 
    (assert (shape-is segiempat)))

(defrule is-segilima
    (sisi 5)
    (sudut 5)
=> 
    (assert (shape-is segilima)))

(defrule is-segienam
    (sisi 6)
    (sudut 6)
=> 
    (assert (shape-is segienam)))

(defrule is-segitiga-siku
    (shape-is segitiga)
    (jenissudut siku-siku)
=>
    (assert (shape-is segitiga-siku)))


(defrule is-segitiga-sama-kaki
    (shape-is segitiga)
    (kesamaansudut 2)
=>
    (assert (shape-is segitiga-sama-kaki)))

(defrule is-segitiga-sama-sisi
    (shape-is segitiga)
    (kesamaansisi lancip)
=>
    (assert (shape-is segitiga-sama-sisi)))

(defrule is-tumpul
    (besarsudut > 90)
=>
    (assert (jenissudut tumpul)))

(defrule is-lancip
    (besarsudut < 90)
=> 
    (assert (jenissudut lancip)))

(defrule is-siku
    (besarsudut = 90)
=>
    (assert (jenissudut siku)))


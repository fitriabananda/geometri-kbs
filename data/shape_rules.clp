
(deftemplate shape
            (slot shape-is)
            (slot jumlahsisi)
            (multislot besarsudut)
            (multislot panjangsisi)
            (slot jenissudut)
)



(defrule is-segitiga
    (jumlahsisi 3)
=> 
    (assert (shape-is segitiga)))

(defrule is-segiempat
    (jumlahsisi 4)
=> 
    (assert (shape-is segiempat)))

(defrule is-segilima
    (jumlahsisi 5)
=> 
    (assert (shape-is segilima)))

(defrule is-segienam
    (jumlahsisi 6)
=> 
    (assert (shape-is segienam)))

(defrule is-segitiga-sama-kaki
    (shape-is segitiga)
    (besarsudut ?sudut1 ?sudut2 ?sudut3)
    (test (or(or(eq ?sudut1 ?sudut2)(eq ?sudut1 ?sudut3))(eq ?sudut2 ?sudut3)))
=>
    (assert(shape-is segitiga-sama-kaki))
)

(defrule is-segitiga-tumpul
    (shape-is segitiga-sama-kaki)
    (jenissudut tumpul)
=>
    (assert (shape-is segitiga-tumpul))
)

(defrule is-segitiga-lancip
    (shape-is segitiga-sama-kaki)
    (jenissudut lancip)
=>
    (assert (shape-is segitiga-lancip))
)

(defrule is-segitiga-siku
    (shape-is segitiga)
    (jenissudut siku)
=>
    (assert (shape-is segitiga-siku)))


(defrule is-segitiga-sama-sisi
    (shape-is segitiga)
    (besarsudut ?s1 ?s2 ?s3)
    (test (eq ?s1 ?s2))
    (test (eq ?s1 ?s3))
=>
    (assert(shape-is segitiga-sama-sisi))
)


(defrule is-tumpul
    (besarsudut ?s1 ?s2 ?s3 )
    (test (or(or(> ?s1 90)(> ?s2 90)) (> ?s3 90)))
=>
    (assert (jenissudut tumpul)))

(defrule is-lancip
    (besarsudut ?s1 ?s2 ?s3 )
    (test (or(or(< ?s1 90)(< ?s2 90)) (< ?s3 90)))
=> 
    (assert (jenissudut lancip)))

(defrule is-siku
    (besarsudut ?s1 ?s2 ?s3 )
    (test (or(or(eq ?s1 90)(eq ?s2 90)) (eq ?s3 90)))
=>
    (assert (jenissudut siku)))


(defrule is-jajar-genjang
    (shape-is segiempat)
    (panjangsisi ?s1 ?s2 ?s3 ?s4)
    (test (and (eq ?s1 ?s2)(eq ?s3 ?s4)))
=>
    (assert (shape-is jajar-genjang))
    )

(defrule is-belah-ketupat
    (shape-is segiempat)
    (shape-is jajar-genjang)
    (panjangsisi ?s1 ?s2 ?s3 ?s4)
    (test (and (eq ?s1 ?s2)(eq ?s3 ?s4)))
    (test (and (eq ?s1 ?s3)(eq ?s1 ?s4)))
=>
    (assert (shape-is belah-ketupat))
    )

(defrule is-layangan
    (shape-is jajar-genjang)
    (besarsudut ?s1 ?s2 ?s3 ?s4)
    (test (or(or(or(eq ?s1 90)(eq ?s2 90))(eq ?s3 90))(eq ?s4 90)))
    (test (or(or(or(< ?s1 90)(< ?s2 90))(< ?s3 90))(< ?s4 90)))
=>
    (assert (shape-is layangan))
    )

(defrule is-segilima-sama
    (shape-is segilima)
    (panjangsisi ?s1 ?s2 ?s3 ?s4 ?s5)
    (test (eq ?s1 ?s2))
    (test(eq ?s1 ?s3))
    (test(eq ?s1 ?s4))
    (test(eq ?s1 ?s5))
=>
    (assert (shape-is segilima-sama))
)

(defrule is-segienam-sama
    (shape-is segienam)
    (panjangsisi ?s1 ?s2 ?s3 ?s4 ?s5 ?s6)
    (test (eq ?s1 ?s2))
    (test (eq ?s1 ?s3))
    (test (eq ?s1 ?s4))
    (test (eq ?s1 ?s5))
    (test (eq ?s1 ?s6))
=>
    (assert (shape-is segienam-sama))
)

(defrule is-trapesium-kaki
    (shape-is segiempat)
    (shape-is ~jajar-genjang)
    (besarsudut ?s1 ?s2 ?s3 ?s4)
    (test (and (eq ?s1 ?s2)(eq ?s3 ?s4)))
    (test (neq ?s1 ?s3))
=>
    (assert (shape-is trapesium-kaki))
    )

(defrule is-trapesium-siku-left
    (shape-is segiempat)
    (shape-is ~jajar-genjang)
    (besarsudut ?s1 ?s2 ?s3 ?s4)
    (test (and(eq ?s2 90)(eq ?s4 90)))
=>
    (assert (shape-is trapesium-siku-left))
    )

(defrule is-trapesium-siku-right
    (shape-is segiempat)
    (shape-is ~jajar-genjang)
    (besarsudut ?s1 ?s2 ?s3 ?s4)
    (test (and(eq ?s1 90)(eq ?s3 90)))
=>
    (assert (shape-is trapesium-siku-right))
    )

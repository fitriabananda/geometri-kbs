
(deftemplate shape
            (slot shape-is)
            (slot jumlahsisi)
            (multislot besarsudut)
            (multislot panjangsisi)
            (slot jenissudut)
            (slot sisisejajar)
)

(defrule try
    (initial-fact)
    =>
    (printout t"BEFORE"crlf) (py_pfact)
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

(defrule is-segitiga-sama-sisi
    (shape-is segitiga)
    (besarsudut ?s1 ?s2 ?s3)
    (test (eq ?s1 ?s2))
    (test (eq ?s1 ?s3))
=>
    (assert(shape-is segitiga-sama-sisi))
)


(defrule is-segitiga-siku
    (shape-is segitiga)
    (jenissudut siku)
=>
    (assert (shape-is segitiga-siku)))

(defrule is-segitiga-sama-kaki
    (shape-is segitiga)
    (besarsudut ?sudut1 ?sudut2 ?)
    (test (eq ?sudut1 ?sudut2))
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

(defrule is-tumpul
    (besarsudut ?sudut)
    (test (> ?sudut 90))
=>
    (assert (jenissudut tumpul)))

(defrule is-lancip
    (besarsudut ?sudut)
    (test (< ?sudut 90))
=> 
    (assert (jenissudut lancip)))

(defrule is-siku
    (besarsudut ?sudut)
    (test (eq ?sudut 90))
=>
    (assert (jenissudut siku)))


(defrule is-jajar-genjang
    (shape-is segiempat)
    (panjangsisi ?s1 ?s2 ?s3 ?s4)
    (test (and (eq ?s1 ?s2)(eq ?s3 ?s4)))
=>
    (assert (shape-is jajar-genjang))
    )

(defrule is-layangan
    (shape-is jajar-genjang)
    (jenissudut siku)
    (jenissudut lancip)
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
=>
    (assert (shape-is trapesium-kaki))
    )

(defrule is-trapesium-siku
    (shape-is segiempat)
    (shape-is ~jajar-genjang)
    (jenissudut siku)
=>
    (assert (shape-is trapesium-siku))
    )



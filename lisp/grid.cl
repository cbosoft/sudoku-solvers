(import 'list)




(defun all? (l)
  "all values true?"
  (if (rest l)
    (and (all? (rest l)) (pop l))
    (pop l)))


(defun count-is-9? (l)
  "is list 9 elements long?"
  (= (count l) 9))


(defun count-rows-is-9? (l)
  " "
  (if (rest l)
    (and (count-is-9? (pop l)) (count-rows-is-9? (rest l)))
    (count-is-9? (pop l))))


(defun grid? (g)
  "check if object G is a 9x9 sudoku grid"
  (and (count-is-9? g) (count-rows-is-9? g)))


(print (count '(1 2 3)))


(print (grid? '(
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                )))

(print (grid? '(
                ( 1 0 0 0 0 0 0 0 0 )
                ( 0 1 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                )))

(print (grid? '(
                ( 1 0 0 0 0 0 0 0 0 )
                ( 0 1 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                )))

(print (grid? '(
                ( 1 0 0 0 0 0 0 0 0 )
                ( 0 1 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 0 0 0 0 0 )
                ( 0 0 0 0 1 0 0 0 0 )
                )))

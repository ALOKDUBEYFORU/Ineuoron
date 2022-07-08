import logging
logging.basicConfig(filename="Strings_task.log",level = logging.INFO,
                    format='%(name)s %(asctime)s %(levelname)s %(message)s')

class Stringstask:
    '''
    Stringstask class is defined for writing the function to perform the above tasks. \n
    Public Variable :
        stringval : Used to capture a string value and this value is further used in the methods for transformation.\n \n

    Methods :
        task1 : Takes an input of the stringvalue and is used to return the value from index one to index 300 with a jump of 3. \n
        task2 : Takes an input of the stringvalue and is used to return the reverse value of a string without using reverse function. \n
        task3 : Takes an input of the stringvalue and is used to return the string formed by splitting a string after conversion of entire string in uppercase. \n
        task4 : Takes an input of the stringvalue and is used to return the string in lower case. \n
        task5 : Takes an input of the stringvalue and is used to return the string in capitalize case. \n
        task7 : Takes an input of the stringvalue and is used to return the string returned after passing it to expand tab. \n
        task8 : Takes an input of the stringvalue and is used to return the string output of strip , lstrip and rstrip. \n
        task9 : Takes an input of the stringvalue and is used to return the new string after replacing a character by another character. \n
        task10 : Takes an input of the stringvalue and is used to return the new string after applying the string center function. \n
    '''
    logging.info("Beginning of the StringTask class")

    def __init__(self,s = "this is My First Python programming class and i am learNING python string and its function") :
        '''
        Constructor to initialize the object variable named as stringval
        :param s: A default value had been assigned and can be overwritten by the user, if needed.
        '''
        try :
            logging.info("Beginning of the constructor method of the Stringstask class")
            logging.info("Prior to assigning the parameter value to the class variable ('%s') ",s)
            self.stringval = s
            logging.info("Assignment had been completed with the value '%s'",self.stringval)
        except Exception as e:
            logging.error("Exception had been raised in the constructor of Stringtask class",e)
        finally :
            logging.info("The constructor of the Stringstask had been executed")

    def task1(self):
        '''
        This function is defined in the Stringstask class
        for extracting data from index one to index 300 with a jump of 3 from the stringval variable of the
        the class
        :return : a value of a string
        '''
        try :
            logging.info("Starting of the task1 method of Stringstask class")
            logging.info("before evaluating '%s[1:300:3]' and assigning it to the local variable "
                         "string1",self.stringval)
            string1 = self.stringval[1:300:3]
            logging.info("slicing had been completed "
                         "returning the value '%s' string1 variable ",string1)
            return string1
        except Exception as e :
            logging.error("An exception had occured in executing the task1 method of the Stringtask class",e)
        finally :
            logging.info("completion of the task1 method of Stringtask class")

    def task2(self):
        '''Task2 method in Stringstask is written to reverse a string without using reverse function
        :return : String
        '''
        logging.info("Beginning of the task2 method of Stringstask class")
        try :
            logging.info("try block in the task2 method of Stringstask class had been initiated")
            logging.info("Initializing the local variable by using the slicing function to reverse "
                         "the stringval variable i.e.. '%s[::-1]'",self.stringval)
            reversestring = self.stringval[::-1]
            logging.info("The string had been reversed and returning the value of "
                         "reversestring i.e..,'%s'",reversestring)
            return reversestring
        except Exception as e :
            logging.Error("Exception had been raised while reversing the string ",e)
        finally :
            logging.info("task2 method of Stringstask had been completed")

    def task3(self):
        '''
        task3 method of Stringstask had been written for splitting a string after conversion of entire string in uppercase
        :return : string
        '''
        logging.info("Beginning of the task3 method of Stringstask")
        try :
            logging.info("Before converting the string into upper case and splitting")
            splitstring = self.stringval.upper().split(" ")
            logging.info("string value had been converted into the uppercase and had been splitted")
            logging.info("Returning the splitstring value")
            return splitstring
        except Exception as e :
            logging.error("exception occured in the task3 method of Stingstask ",e)
        finally :
            logging.info("end of the task3 method of Stringstask class")

    def task4(self):
        '''
        Task4 method of Stringstask class is used to convert the whole string into lower case
        :return : string
        '''
        logging.info("starting of the task4 method of Stringstask class")
        try:
            logging.info("converting the variable in the lower case")
            return self.stringval.lower()
        except Exception as e :
            logging.error("Exception occured in the task4 method of Stringtask class ",e)
        finally :
            logging.info("End of the task4 method of Stringstask class")

    def task5(self):
        '''
        The task5 method of Stringstask is used to capitalize the whole string
        :return : string
        '''
        logging.info("Starting of the task5 method of Stringstask class")
        try :
            logging.info("returning the captialized string")
            return self.stringval.capitalize()
        except Exception as e :
            logging.error("Exception occured in the task5 method of Stringstask class ",e)
        finally :
            logging.info("End of the task5 method of Stringstask class ")


    def task7(self):
        '''
        Try to give an example of expand tab
        :return: string
        '''
        logging.info("starting of the task7 method of Stringstask class")
        try :
            logging.info("returning the value of a string with expanded tabs method")
            return "\tI\tam\tavailable".expandtabs()
        except Exception as e:
            logging.error("Exception had occured in the task7 method of Stringstask class ",e)
        finally :
            logging.info("End of the task7 method of Stringstask class")

    def task8(self):
        '''
        Give an example of strip , lstrip and rstrip
        :return: tuple
        '''
        logging.info("Starting of the task8 method of Stringstask class")
        try :
            logging.info("defining three variables with the values '  test1 test2 '")
            lvstring1 = '  test1 test2 '
            logging.info('declaring three variables to hold the values when strip ,lstrip and rstrip is applied')
            lvstrip1,lvlstrip1,lvrstrip1 = (lvstring1.strip(),lvstring1.lstrip(),lvstring1.rstrip())
            logging.info("the outputs are: '%s';'%s';'%s';",lvstrip1,lvlstrip1,lvrstrip1)
            return lvstrip1,lvlstrip1,lvrstrip1
        except Exception as e:
            logging.Error("Error had occured in the metho task8 method of Stringstask class ",e)
        finally :
            logging.info("End of the task8 method of Stringstask class")

    def task9(self, pstringval,poldstring='a',pnewstring='p'):
        '''
        The method task9 of Stringstask class is used to replace a string charecter by another charector by taking your own example
        :param pstringval: This is the string which will be replaced
        :param poldstring : This specifies the string that needs to be replaced
        :param pnewstring : This provides the string that will replace string provided in poldstring
        :return: string
        '''
        logging.info("beginning of task9 method of Stringstask class")
        try :
            logging.info("starting the try block. "
                         "calculating the '%s'.replace('%s','%s') ",pstringval,poldstring,pnewstring)
            lvstring = pstringval.replace(poldstring,pnewstring)
            logging.info("returning the value '%s'",lvstring)
            return lvstring
        except Exception as e:
            logging.error("Error occured in task9 method of Stringstask class",e)
        finally:
            logging.info("End of the task9 mether of Stringstask class")
    def task10(self):
        '''
        Task10 method of Stringstask class is to provide an example of string center function
        :return: string
        '''
        logging.info("Beginning of the task10 of Stringstask class")
        try:
            logging.info("Evaluating & returning the value of function 'test'.center(10,'#')")
            return "test".center(10,'#')
        except Exception as e :
            logging.error("Error occured in the execution of task10 of Stringstask class",e)
        finally:
            logging.info("The method task10 of Stringstask class had been executed")

    logging.info("End of the StringTask class")

try :
    logging.info("Main program had started ")
    logging.info("Initializing the object (obj1) of the Stringstask class")
    obj1 = Stringstask()
    logging.info("Object1 had been successfully created")
    logging.info("prior to logging the value of the obj1.stringval")
    logging.info(obj1.stringval)
    logging.info("After logging the value of the obj1.stringval")
    logging.info("Calling the task1 method of Stringstask")
    logging.info(obj1.task1())
    logging.info("task1 method had been executed \n Calling the task2 method of Stringstask class")
    logging.info(obj1.task2())
    logging.info("task2 method had been executed \n Calling the task3 method of Stringstask class")
    logging.info(obj1.task3())
    logging.info("task3 method had been executed \n Calling the task4 method of Stringstask class")
    logging.info(obj1.task4())
    logging.info("task4 method had been executed \n Calling the task5 method of Stringstask class")
    logging.info(obj1.task5())
    logging.info("task5 method had been executed \n Calling the task7 method of Stringstask class")
    logging.info(obj1.task7())
    logging.info("task7 method had been executed \n Calling the task8 method of Stringstask class")
    logging.info(obj1.task8())
    logging.info("task8 method had been executed \n Calling the task9 method of Stringstask class")
    logging.info(obj1.task9("Anupama",'a','b'))
    logging.info("task9 method had been executed \n Calling the task10 method of Stringstask class")
    logging.info(obj1.task10())
    logging.info("task10 method had been executed")
except Exception as e :
    logging.error("Exception had been raised in the main program ",e)
finally :
    logging.info("Reached the end of the main program")

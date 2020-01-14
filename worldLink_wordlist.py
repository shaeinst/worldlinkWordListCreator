import curses

info_dist={
	"Current Created Word" : "",
	"Current testing Word" : "",
	"Created Words Number" : "",
	"total tested Number"  : ""
}
onlyChar_List = ["A", "B", "C", "D", "E", "F"]
onlyNum_List  = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



#------------------------------------------------------------------------
#					OUTPUT FILE
#------------------------------------------------------------------------
def wordlist_file():
	wordlist=open(f"word_list.txt", "w") #directory to save the created wordlist
	return wordlist
#------------------------------------------------------------------------
#					end of OUTPUT FILE
#------------------------------------------------------------------------





#------------------------------------------------------------------------
#					CHAR COUNTER
#------------------------------------------------------------------------
def count(word, char):
	i=0
	for letter in word:
		if letter==char:
			i += 1
	return i
#------------------------------------------------------------------------
#					end of CHAR COUNTER
#------------------------------------------------------------------------



#------------------------------------------------------------------------
#					PRINT INFORMATION ON SCREEN
#------------------------------------------------------------------------
def onScreen(cw, cwn, testing_word, total_tested_num):		
	scr = curses.initscr()
	toPrint="\n\n\n\nCurrent Created Word => %10s\nCurrent Testing Word => %10s\n\nCreated Words Number => %11s\nTotal Tested Number  => %11s" %(cw, testing_word, cwn, total_tested_num)
	scr.addstr(0, 0, toPrint)
	scr.refresh()


#------------------------------------------------------------------------
#					end of PRIN INFORMATION ON SCREEN
#------------------------------------------------------------------------




#------------------------------------------------------------------------
#						HEX CONVERTER
#------------------------------------------------------------------------
class HexCL:
	#NUM TO HEX CONVERTER
	def hex_converter(num_h):
		num_h = hex(num_h).upper()
		num_h = num_h[2:]
		return num_h

	# HEX + CL   
	def CL_Num(num_c):
		return "CL"+num_c

	def HCL(num):
		num = HexCL.hex_converter(num)
		num = HexCL.CL_Num(num)
		return num
#------------------------------------------------------------------------
#						end of HEX CONVERTER
#------------------------------------------------------------------------



#------------------------------------------------------------------------
#						ALGORITHM
#------------------------------------------------------------------------
class filter_Algorithm:

	def thirdMustChar(word):
		if word[2] in onlyChar_List:
			return True
		return False


	def charMustMax(word):  # number of characters (in a word) must be equal 
		char_num = 0		# or greater than base10num(0,1,2,3,4,5,6,7,8,9)
		num_num = 0
	
		for letter in word:  
			if letter not in onlyChar_List:
				if letter in onlyNum_List:
					num_num += 1
				continue
			char_num += 1

		if char_num >= num_num: # change num_num to num_num-1 for cahr_num>=num_num
			return True
		return False


	def MustBeNum(word):
		num=0
		for letter in word:
			if letter not in onlyNum_List:
				continue
			num += 1
		if num<2:
			return False
		return True


	def sameChar(word):
		for letter in word:
			if count(word, letter) > 4:
				return True
		return False
 	

	def Rerepeted(word):
		i=0
		count=0
			
		while i < 6:
			if word[i+2]==word[i+3]==word[i+4]:
				count += 1
			i += 1
		if count > 1:
			return True
		return False


	def _3x_Repeted(word):
		i=0
		count=0
			
		while i < 6:
			if word[i+2] in onlyNum_List or word[i+2] in onlyChar_List:
				if word[i+2]==word[i+3]==word[i+4]:
					count += 1
					break
			i += 1			

		if count > 0:
			return True
		return False


	def four_Rerepeted(word):
		i=0
		j=0
		count=0
				
		while i < 7:
			if word[i] in onlyNum_List and word[i+1] in onlyNum_List and word[i+2] in onlyNum_List and word[i+3] in onlyNum_List:
				count += 1
				break
			i += 1

			if word[j] in onlyChar_List and word[j+1] in onlyChar_List and word[j+2] in onlyChar_List and word[j+3] in onlyChar_List:
				count += 1
				break
			j += 1

		if count > 0:
			return True
		return False

#------------------------------------------------------------------------
#						end of algorithm
#------------------------------------------------------------------------





def WordList(total_word=999999999, start_num=2684354560): # 2684354560
	count			 = 1				#for tracking the number of created words
	total_tested_num = 0				#for tracking how much words has been tested
	wordlist         = wordlist_file()	#file location and name setting up

	while True:
		HCL = HexCL.HCL(start_num)

		info_dist["Current testing Word"] = HexCL.HCL(start_num)
		info_dist["total tested Number"]  =  total_tested_num

		testing_word 	 = info_dist["Current testing Word"]
		total_tested_num = info_dist["total tested Number"]
		cw 				 = info_dist["Current Created Word"]
		cwn				 = info_dist["Created Words Number"]

		start_num += 1
		total_tested_num += 1

		# os.system("clear") #clear the screeen, NOT USING BECAUSE IT SLOW DOWN THE PROCESSING
		onScreen(cw, cwn, testing_word, total_tested_num)

		if len(HCL) != 10:
			if len(HCL) < 10:
				continue
			if len(HCL) > 10:
				break

		#applying filter Algorithm
		charMustMax    = filter_Algorithm.charMustMax(HCL)
		MustBeNum 	   = filter_Algorithm.MustBeNum(HCL)
		sameChar 	   = filter_Algorithm.sameChar(HCL)
		Rerepeted 	   = filter_Algorithm.Rerepeted(HCL)
		four_Rerepeted = filter_Algorithm.four_Rerepeted(HCL)
		thirdMustChar  = filter_Algorithm.thirdMustChar(HCL)
		_3x_Repeted    = filter_Algorithm._3x_Repeted(HCL)

		if not thirdMustChar or not charMustMax or _3x_Repeted or four_Rerepeted or Rerepeted or not MustBeNum or sameChar:	
			continue

		wordlist.write(HCL+"\n")	# writing the words which has been accepted (by Algorithm)
		count += 1 

		info_dist["Current Created Word"] = HCL
		info_dist["Created Words Number"] = count

		cw  = info_dist["Current Created Word"]
		cwn = info_dist["Created Words Number"]

		if count > total_word:
			break

	wordlist.close()	
	print("Created Wordlist Saved")


try:
	WordList()	# WordList(no_of_words, starting_base10_num)
except KeyboardInterrupt:
	print("\n\nhave a nice day!!!")

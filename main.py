#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Coded By Kuduxaaa
from wget import download,bar_adaptive
from playsound import playsound
from requests import get,post
from json import loads
import wikipedia
import os,sys

შედეგები = {}

def ლაპარაკი(რა):
  პასუხი = post(url="http://test-voice.sda.gov.ge/DesktopModules/Voice/VoiceService.asmx/Speak", headers={"Content-Type": "application/json; charset=utf-8"}, json={"argText":str(რა),"argRate":"40"})
  აუდიოს_ბმული = str(f'http://test-voice.sda.gov.ge{loads(str(პასუხი.text))["d"][0]}')
  download(აუდიოს_ბმული, bar=bar_adaptive(0,0,0))
  ფილის_სახელი = აუდიოს_ბმული.split("/")[-1]
  playsound(ფილის_სახელი)
  os.remove(ფილის_სახელი)

def ძებნა(კითხვა):
  global შედეგები
  ინკრემენტა = 1
  wikipedia.set_lang("ka")
  ძებნის_შედეგები = wikipedia.search(კითხვა)
  if bool(ძებნის_შედეგები):
    for ძებნის_შედეგი in ძებნის_შედეგები:
  	  print(f"[{ინკრემენტა}] {ძებნის_შედეგი}")
  	  შედეგები[ინკრემენტა] = ძებნის_შედეგი
  	  ინკრემენტა += 1
  else:
  	os.system("cls" if os.name == "nt" else "clear")
  	print("უკაცრავად... ვერაფერი მოვძებნე!\nსცადეთ სხვა საძიებო სიტყვა")
  	სტარტი()

def შესახებ(შედეგის_ინდექსი):
  global შედეგები
  wikipedia.set_lang("ka")
  ლაპარაკი(wikipedia.summary(შედეგები[შედეგის_ინდექსი]))

def სტარტი():
  print("თქვენ იმყოებით საძიებო ხელსაწყო ჯეოვიკში\nშეიყვანეთ საძიებო სიტყვა ^^\n")
  while True:
    კითხვა = input("აბა რას ვეძებთ? /> ")
    print("აირჩიეთ ერთ-ერთი ნუმერაციით")
    ძებნა(კითხვა)
    ინდექსი = int(input("\nრომელი წაგიკითხოთ? /> "))
    print("წავიკიტხავ და წაგიკითხავ :D\nორი წამით... ")
    შესახებ(ინდექსი)
    გამეორება = input("კიდევ გსურთ რამზე ინფორმაციის მოძიება (კი/არა)")
    if გამეორება == "კი":სტარტი()
    else:sys.exit("კარგით, კარგად ბრძანდებოდეთ <3")

if __name__ == '__main__':
	print("გამარჯობა, ", end="")
	os.system("cls" if os.name == "nt" else "clear")
	try:სტარტი()
	except Exception as შეცდომა:sys.exit(შეცდომა)
function getScripture(){
  randBook = Math.floor(Math.random() * 67);
  randChapter = Math.floor(Math.random() * 151);
  randVerse = Math.floor(Math.random() * 177);
  var bookName = ["Genesis",
  "Exodus",
  "Leviticus",
  "Numbers",
  "Deuteronomy",
  "Joshua",
  "Judges",
  "Ruth",
  "1 Samuel",
  "2 Samuel",
  "1 Kings",
  "2 Kings",
  "1 Chronicles",
  "2 Chronicles",
  "Ezra",
  "Nehemiah",
  "Esther",
  "Job",
  "Psalms",
  "Proverbs",
  "Ecclesiastes",
  "Song of Solomon",
  "Isaiah",
  "Jeremiah",
  "Lamentations",
  "Ezekiel",
  "Daniel",
  "Hosea",
  "Joel",
  "Amos",
  "Obadiah",
  "Jonah",
  "Micah",
  "Nahum",
  "Habakkuk",
  "Zephaniah",
  "Haggai",
  "Zechariah",
  "Malachi",
  "The New Testament",
  "Matthew",
  "Mark",
  "Luke",
  "John",
  "Acts",
  "Romans",
  "1 Corinthians",
  "2 Corinthians",
  "Galatians",
  "Ephesians",
  "Philippians",
  "Colossians",
  "1 Thessalonians",
  "2 Thessalonians",
  "1 Timothy",
  "2 Timothy",
  "Titus",
  "Philemon",
  "Hebrews",
  "James",
  "1 Peter",
  "2 Peter",
  "1 John",
  "2 John",
  "3 John",
  "Jude",
  "Revelation"]
  var bookNumSearch = randBook - 1;
  var randBookName = bookName[bookNumSearch];
  console.log(randBookName);
  vargetScripture = randBookName + " " + randChapter + ":" + randVerse;
  vargetScriptureLink = new String("https://bible-api.com/" + randBookName + "+" + randChapter + ":" + randVerse);
  console.log(vargetScripture)
  console.log(vargetScriptureLink)
  vargetScriptureOutput = vargetScripture + "<br>" + vargetScriptureLink

  return vargetScriptureOutput;
}

// get book number then
// if book number then random var set to how many chapters in that book
//then if chapter, random var set to how many verses in that chapter 

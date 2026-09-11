from collections import OrderedDict


def p(text):
    return " ".join(text.strip().split())


def q(num, stem, choices, answer, explanation):
    return {"num": num, "stem": p(stem), "choices": [p(x) for x in choices], "answer": answer, "explanation": p(explanation)}


SETS = []

# -----------------------------------------------------------------------------
# SET 1: DETECTIVE CONAN — 2021 remake E1000–E1001, Moonlight Sonata case
# Verified against Crunchyroll episode descriptions for E1000 and E1001.
# -----------------------------------------------------------------------------
conan = {
    "slug": "detective_conan_moonlight",
    "display_title": "DETECTIVE CONAN",
    "jp_title": "『名探偵コナン』―「月光」事件 Special Practice Set",
    "episode_label": "The Moonlight Sonata Murder (2021 remake, Episodes 1000–1001)",
    "intro_jp": "『名探偵コナン』は、少年の姿になった高校生探偵が数々の事件に挑むミステリー作品です。今回は、月影島へ届いた不可解な依頼と『月光』の旋律が結び付く代表的な事件を題材にします。作品を知らなくても、必要な情報はすべて本文中に示してあります。",
    "background_en": p("""
        Conan, Ran, and Kogoro travel to Moonshade Island after a letter asks them to investigate a strange matter. The request is already unusual because the person named as the client is a pianist who was said to have died twelve years earlier while playing Beethoven's "Moonlight Sonata." On the island, a memorial service is being held at the community center, and the same piece of music is heard again. The case becomes more serious when the current mayor is found dead and a musical score written in blood appears. This practice set uses those verified events as the basis for original English reading tasks. The questions focus on how clues gain meaning from timing, sequence, and connections with other evidence rather than on knowledge that only fans would have.
    """),
    "names": [
        ("江戸川コナン", "Conan"),
        ("毛利 蘭", "Ran"),
        ("毛利小五郎", "Kogoro"),
        ("月影島", "Moonshade Island"),
        ("ピアノソナタ『月光』", "Moonlight Sonata"),
    ],
    "source_note_internal": "Crunchyroll Detective Conan E1000 and E1001 episode descriptions; used only for fact verification.",
}

conan["part1"] = [
    q(1, "The letter was especially ( ) because it seemed to have been sent by a pianist who had died years earlier.",
      ["ordinary", "mysterious", "narrow", "patient"], 2,
      "正解は2 mysterious「謎めいた」。死亡したとされる人物から届いたように見える手紙なので文脈に合う。ordinaryは「普通の」、narrowは「狭い」、patientは「我慢強い」。"),
    q(2, "Conan did not ignore the strange letter. He decided to ( ) who had actually sent it and why.",
      ["replace", "celebrate", "divide", "investigate"], 4,
      "正解は4 investigate「調査する」。送信者と目的を調べる文脈。replaceは「取り替える」、celebrateは「祝う」、divideは「分ける」。"),
    q(3, "When the Moonlight Sonata began to play at the memorial service, the music became an important ( ) in the case.",
      ["clue", "harvest", "bargain", "shelter"], 1,
      "正解は1 clue「手がかり」。事件の判断材料になる音楽を指す。harvestは「収穫」、bargainは「お買い得品／取引」、shelterは「避難所」。"),
    q(4, "The visitors were ( ) when music connected to a dead pianist suddenly filled the room.",
      ["grateful", "independent", "uneasy", "humorous"], 3,
      "正解は3 uneasy「不安な、落ち着かない」。不気味な状況で突然流れる音楽に合う。gratefulは「感謝して」、independentは「独立した」、humorousは「ユーモラスな」。"),
    q(5, "Conan carefully ( ) small details instead of accepting the islanders' first explanation.",
      ["borrowed", "observed", "repaired", "floated"], 2,
      "正解は2 observed「観察した」。細部を注意深く見るという意味。borrowedは「借りた」、repairedは「修理した」、floatedは「浮かんだ」。"),
    q(6, "The pianist had ( ) died twelve years earlier, so his name on the new request was surprising.",
      ["supposedly", "politely", "widely", "safely"], 1,
      "正解は1 supposedly「～だとされて、伝えられて」。死亡したと報じられていた、という含みになる。politelyは「丁寧に」、widelyは「広く」、safelyは「安全に」。"),
    q(7, "The current mayor was found dead, so the investigation became more ( ) than the unusual letter had first suggested.",
      ["familiar", "private", "gentle", "serious"], 4,
      "正解は4 serious「重大な、深刻な」。死亡事件が起きたため、当初より深刻になる。familiarは「よく知られた」、privateは「私的な」、gentleは「穏やかな」。"),
    q(8, "A musical score written in blood was not just a decoration; Conan treated it as possible ( ).",
      ["scenery", "luggage", "evidence", "permission"], 3,
      "正解は3 evidence「証拠」。現場に残された楽譜を事件解明の材料として扱う。sceneryは「景色」、luggageは「手荷物」、permissionは「許可」。"),
    q(9, "Because the same piece of music appeared again, Conan considered whether the events were ( ).",
      ["temporary", "connected", "generous", "noisy"], 2,
      "正解は2 connected「関連している」。同じ曲の反復から出来事同士のつながりを検討する文脈。temporaryは「一時的な」、generousは「気前のよい」、noisyは「騒がしい」。"),
    q(10, "Conan tried to read the message carefully rather than ( ) what it meant.",
      ["preserving", "delivering", "borrowing", "guessing"], 4,
      "正解は4 guessing「推測すること」。証拠を読んで判断することと、根拠なく推測することの対比。preservingは「保存する」、deliveringは「届ける」、borrowingは「借りる」。"),
    q(11, "The group came to the island ( ) a request that had arrived by letter.",
      ["in response to", "at the edge of", "in place of", "by means of"], 1,
      "正解は1 in response to「～に応じて」。手紙の依頼を受けて島へ来たという意味。at the edge ofは「～の端に」、in place ofは「～の代わりに」、by means ofは「～によって」。"),
    q(12, "The client had reportedly died years earlier, so the request did not ( ) at first.",
      ["take place", "turn around", "make sense", "grow up"], 3,
      "正解は3 make sense「筋が通る、意味を成す」。死亡した人物からの依頼は最初は筋が通らない。take placeは「起こる」、turn aroundは「振り向く／好転する」、grow upは「成長する」。"),
    q(13, "Conan had to ( ) several details—the letter, the music, and the score—without assuming they all meant the same thing.",
      ["run out of", "look down on", "get away with", "keep track of"], 4,
      "正解は4 keep track of「～を把握し続ける」。複数の手がかりを整理して追う文脈。run out ofは「～を使い果たす」、look down onは「～を見下す」、get away withは「～をして罰を免れる」。"),
    q(14, "When the music began during the memorial, everyone had to ( ) the timing of the sound.",
      ["take care of", "pay attention to", "come down with", "make up for"], 2,
      "正解は2 pay attention to「～に注意を払う」。音が鳴った時点に注目する。take care ofは「～の世話をする」、come down withは「病気にかかる」、make up forは「～を埋め合わせる」。"),
    q(15, "The new death seemed to ( ) the island's older story about the pianist.",
      ["be connected with", "be proud of", "be absent from", "be satisfied with"], 1,
      "正解は1 be connected with「～と関連している」。新しい事件と過去のピアニストの話の関連を示す。be proud ofは「～を誇りに思う」、be absent fromは「～を欠席する」、be satisfied withは「～に満足する」。"),
    q(16, "Instead of jumping to a conclusion, Conan tried to ( ) the message left at the scene.",
      ["get over", "put off", "make sense of", "take after"], 3,
      "正解は3 make sense of「～を理解する」。現場のメッセージを解釈する文脈。get overは「～を乗り越える」、put offは「延期する」、take afterは「～に似る」。"),
    q(17, "Each new clue could ( ) a different possible explanation, so Conan had to decide what to examine next.",
      ["settle for", "point to", "carry on", "break down"], 2,
      "正解は2 point to「～を示す、示唆する」。新しい手がかりが別の可能性を示す。settle forは「～で妥協する」、carry onは「続ける」、break downは「故障する／分解する」。"),
]

conan["part2a"] = {
    "title": "A Letter That Should Not Exist",
    "paragraphs": [
        p("""Conan, Ran, and Kogoro travel to Moonshade Island after receiving a letter asking them to come there. The request is strange because the person named as the client is a pianist who was reported to have died twelve years earlier. In an ordinary request, the sender's identity helps explain why a detective is needed. Here, the identity itself creates the first mystery. Instead of treating the letter only as directions to an island, the investigators must ( 18 ). The contradiction makes the sender, the timing, and the purpose of the letter part of the case."""),
        p("""When the three arrive, they go to a community center where a memorial service for the previous mayor is being held. During the service, Beethoven's "Moonlight Sonata" begins to play. The piece matters because the pianist connected to the letter was said to have died while playing it. The sound therefore links a present event with a story from twelve years before. For Conan, the music does not prove who is responsible. Instead, ( 19 )."""),
        p("""Later, the current mayor is found dead, and a musical score written in blood appears at the scene. Conan is able to read a message from it. By this point, the unusual letter, the music, and the written score cannot simply be treated as separate odd events. ( 20 ), each new piece of information changes how the earlier clues may be understood. The case grows not because one clue gives an immediate answer, but because several clues begin to form a pattern that must be explained."""),
    ],
    "questions": [
        q(18, "", ["accept the island trip as ordinary sightseeing", "assume the pianist returned without any evidence", "focus only on the handwriting of the letter", "consider who could have sent it and for what purpose"], 4,
          "正解は4。死亡したとされる人物の名で依頼が届いたため、送り主と目的そのものを調べる必要がある。1は依頼の異常性を無視し、2は根拠のない断定、3は本文の焦点を狭めすぎている。"),
        q(19, "", ["it turns an old story into a current clue that still needs explanation", "it proves that the dead pianist is secretly alive", "it shows that the memorial guests planned a concert", "it makes the original letter unimportant"], 1,
          "正解は1。曲は過去の死亡と現在を結び付けるが、それだけで犯人や原因は確定しない。2は証明しすぎ、3は本文にない、4は逆に手紙の重要性を下げている。"),
        q(20, "", ["In contrast", "For example", "As a result", "At first"], 3,
          "正解は3 As a result「その結果」。複数の手がかりが一つの流れとして見え始めた結果、後の情報が前の手がかりの意味を変える、という因果関係。"),
    ],
    "translation": [
        "コナン、蘭、小五郎は、島へ来てほしいという手紙を受け取り、月影島へ向かいます。ところが、その依頼は奇妙でした。依頼人として名前が記されていたのは、12年前に亡くなったとされるピアニストだったからです。普通の依頼なら、送り主が誰なのか分かれば、なぜ探偵が必要なのかもある程度見えてきます。しかし今回は、その送り主の正体そのものが最初の謎になっています。そこで一行は、手紙を単なる島への案内として受け取るのではなく、誰が何の目的で送ったのかを考えなければなりません。この矛盾によって、送り主、手紙が届いた時期、そして依頼の目的までが事件の一部になります。",
        "3人が島に着くと、前の村長の法要が行われている公民館へ向かいます。その最中に、ベートーベンの『月光』が流れ始めます。この曲が重要なのは、手紙と関係するピアニストが、12年前にこの曲を弾きながら亡くなったとされているためです。つまり、その音楽は現在起きている出来事と12年前の話を結び付けます。ただし、コナンにとって、曲が流れたという事実だけでは、誰が何をしたのかまでは分かりません。むしろ、過去の出来事が、いま改めて説明しなければならない手がかりとして浮かび上がってくるのです。",
        "その後、現職の村長が遺体で発見され、現場には血で書かれた楽譜が残されています。コナンは、そこに込められたメッセージを読み取ります。この時点になると、不可解な手紙、流れた音楽、そして楽譜を、ただの別々の奇妙な出来事として扱うことはできません。その結果、新しい情報が加わるたびに、それまでの手がかりの意味も変わって見えてきます。この事件が複雑になっていくのは、一つの手がかりがすぐ答えを与えるからではありません。複数の手がかりが、説明すべき一つのパターンを形作り始めるからです。",
    ],
}

conan["part2b"] = {
    "title": "A Clue That Can Be Heard",
    "paragraphs": [
        p("""Music can work as a very different kind of clue from a letter or a written message. When the "Moonlight Sonata" begins during the memorial service on Moonshade Island, many people can hear the same sound at about the same time. A sound can therefore create a shared moment in a mystery. In this case, the melody also recalls the pianist who was believed to have died years earlier while playing it. Because of this connection, ( 21 )."""),
        p("""However, a clue that many people notice is not necessarily a clue that explains itself. Several witnesses may agree that they heard the same piece, but that agreement does not show who caused the music to play or why it was chosen. The observation and the explanation are different. ( 22 ). A careful investigator therefore has to separate what was directly heard from the meaning people give to it."""),
        p("""After the current mayor is found dead, a blood-written musical score provides another kind of information. Unlike the music, the score is a visible object that can be examined and interpreted as a message. Conan can compare this new clue with the letter and the repeated use of the same piece of music. ( 23 ), the importance of the melody becomes clearer when it is considered together with other evidence rather than by itself."""),
    ],
    "questions": [
        q(21, "", ["the song proves that every person at the memorial is a suspect", "the sound can direct several people's attention to the same unusual event", "the visitors can identify the person who started the music immediately", "the melody makes written evidence unnecessary"], 2,
          "正解は2。同じ時間に多くの人が聞く音は、複数の人の注意を同じ出来事へ向ける。1・3は曲だけで断定しすぎ、4は後段の楽譜の重要性と矛盾する。"),
        q(22, "", ["A famous piece of music is always more useful than a written clue", "Witnesses usually remember music in exactly the same way", "The melody can show that no one in the room caused the event", "A clear observation may still allow more than one explanation"], 4,
          "正解は4。『聞いた』という観察が一致しても、誰がなぜ流したかは複数の説明があり得る、という段落の論点。1・2・3は本文が述べていない。"),
        q(23, "", ["For this reason", "In the past", "By accident", "On average"], 1,
          "正解は1 For this reason「この理由から」。楽譜という別種の証拠と照合できるため、曲の意味がより明確になるという因果。"),
    ],
    "translation": [
        "音楽は、手紙や書かれたメッセージとはかなり違う形で手がかりになります。月影島の法要の最中に『月光』が流れ始めると、その場にいる多くの人が、ほぼ同じ時間に同じ音を聞くことができます。そのため音は、ミステリーの中で複数の人が共有する一つの瞬間を作り出せます。さらにこの事件では、その曲が、何年も前に同じ曲を弾きながら亡くなったとされるピアニストを思い起こさせます。こうしたつながりがあるため、その音は、複数の人の注意を同じ不可解な出来事へ向けることができます。",
        "しかし、多くの人が気付く手がかりだからといって、それ自体が意味を説明してくれるわけではありません。何人もの目撃者が同じ曲を聞いたことには同意できても、その事実だけでは、誰が曲を流したのか、なぜその曲が選ばれたのかまでは分かりません。観察した事実と、その事実の説明は別のものです。つまり、はっきり確認できた出来事であっても、そこから考えられる説明は一つとは限りません。だからこそ、慎重な捜査では、実際に聞こえたことと、人々がそこに与える意味とを分けて考える必要があります。",
        "現職の村長が死亡しているのが見つかった後、血で書かれた楽譜という別の種類の情報が現れます。音楽とは異なり、楽譜は目で確認できる物であり、調べたうえでメッセージとして解釈することができます。コナンは、この新しい手がかりを、手紙や、同じ曲が繰り返し使われていることと比べることができます。このため、『月光』という旋律の重要性は、それだけを単独で見るよりも、ほかの証拠と合わせて考えたときに、よりはっきりしてくるのです。",
    ],
}

conan["part3a"] = {
    "headers": {
        "From": "Aiko Sato <aiko@citymysterymuseum.example>",
        "To": "Daniel Lee <dlee@greenhillhs.example>",
        "Date": "September 10",
        "Subject": "Moonshade Island mystery workshop",
    },
    "greeting": "Dear Daniel,",
    "paragraphs": [
        p("""Thank you for agreeing to bring your English club to our Detective Conan mystery workshop next Friday. The activity is inspired by the Moonlight Sonata case. Visitors will work in teams and move through three stations. At the first station, they will receive a letter from a client who is described as already dead. At the second, a recording of the Moonlight Sonata will play while teams study a short timeline. At the third, they will examine a copy of a musical score containing a coded message. We changed the order after our trial session because students who saw the score first could guess too much about the later tasks."""),
        p("""Please arrive by 1:30 p.m. so we can make teams of four or five before the 2:00 start. Students should bring pencils, but they should keep their phones in their bags during the activity. The music will play through speakers, so headphones are not necessary. Each station will take about twelve minutes, and the whole program will end before 3:30."""),
        p("""Could one teacher stay near Station Two? Please remind teams that hearing the same music does not tell them who started it. However, do not explain the solution. We want students to use only the information in the workshop materials, even if they already know the anime episode."""),
    ],
    "closing": "Best wishes,\nAiko Sato\nCity Mystery Museum",
    "questions": [
        q(24, "Why did the museum change the order of the three stations?", ["To make the music play for a longer time", "To reduce the number of students at the workshop", "To prevent an early clue from making later tasks too easy", "To let students use their phones at the final station"], 3,
          "正解は3。試行時に楽譜を先に見せると、その後の課題を推測しやすくなったため順番を変更した。1・2・4はメールにない。"),
        q(25, "What does Aiko say about the equipment for the workshop?", ["Every student must bring headphones", "Students do not need headphones because the music will play through speakers", "The school must provide a projector for Station Three", "Students may use phones to record the music"], 2,
          "正解は2。音楽はスピーカーから流れるのでヘッドホン不要と明記。1は逆、3は記載なし、4は携帯をバッグに入れる指示と矛盾。"),
        q(26, "Why does Aiko want a teacher near Station Two?", ["To remind teams not to confuse hearing the music with knowing who caused it", "To choose which students are allowed to hear the recording", "To explain the solution before teams reach the final station", "To collect students' phones and return them after the program"], 1,
          "正解は1。音を聞いた事実と、その原因を特定することを区別させるため。3は『解答を説明しない』に反し、2・4は依頼されていない。"),
    ],
    "translation": [
        "ダニエルへ\n\n来週金曜日に、あなたの英語クラブを『名探偵コナン』のミステリー・ワークショップへ連れてきてくださることになり、ありがとうございます。今回の活動は『月光』事件をもとにしています。参加者はチームで3つのステーションを順番に回ります。第1ステーションでは、すでに亡くなっていると説明された依頼人からの手紙を受け取ります。第2ステーションでは、『月光』の録音を聞きながら短い時系列表を確認します。第3ステーションでは、暗号のメッセージが入った楽譜の写しを調べます。試行会では、楽譜を最初に見た生徒が後の課題を推測しすぎてしまったため、今回は順番を変更しました。",
        "午後2時の開始前に4～5人のチームを作れるよう、午後1時30分までに来てください。生徒は鉛筆を持参してください。ただし、活動中は携帯電話をバッグに入れておくようお願いします。音楽はスピーカーから流すので、ヘッドホンは必要ありません。各ステーションは約12分で、プログラム全体は午後3時30分までに終了します。",
        "第2ステーションの近くに先生が1人いていただけますか。『同じ音楽を聞いた』というだけでは、『誰がその音楽を流したのか』までは分からない、という点をチームに思い出させてください。ただし、答えそのものは説明しないでください。すでにアニメのエピソードを知っている生徒も、ワークショップ内の資料だけを使って考えるようにしたいと思っています。\n\nよろしくお願いします。\n佐藤愛子\nシティ・ミステリー・ミュージアム",
    ],
}

conan["part3b"] = {
    "title": "How One Clue Changes Another",
    "paragraphs": [
        p("""The 2021 remake of the Moonlight Sonata case begins with a contradiction. Conan, Ran, and Kogoro receive a letter that brings them to Moonshade Island, but the person named as the client is a pianist who was said to have died twelve years earlier. The letter therefore does two jobs at once. It is a practical message that causes the trip, and it is also evidence that something about the situation is not yet understood. Before any new death occurs, the request itself gives the investigators a reason to question what they have been told."""),
        p("""At the community center, a memorial service for the previous mayor is being held when the Moonlight Sonata begins to play. The choice of music is important because the dead pianist was believed to have died while playing the same piece. This connection gives an old story new importance in the present. Still, hearing the music does not identify the person who caused it to play. The episode therefore keeps a useful gap between noticing a connection and proving an explanation."""),
        p("""The situation becomes more serious when the current mayor is found dead. A musical score written in blood is also discovered, and Conan reads a message from it. This clue is different from the music because it is a visible object that can be examined directly. The letter suggested that the past had returned, the music connected past and present, and the score added a message that could be interpreted. Each clue has a different strength and a different limit, so none should simply replace the others."""),
        p("""The order of the clues is one reason the case requires careful reading. If the final message had appeared first, the earlier letter and music might have seemed like decoration. Instead, later information changes the meaning of what came before. A working explanation that seems reasonable after the letter may need to be changed after the music, and changed again after the score. The mystery is therefore not solved by recognizing a famous song. It develops through the repeated task of comparing new evidence with an earlier idea and revising that idea when the evidence no longer fits."""),
    ],
    "questions": [
        q(27, "What does the first paragraph emphasize about the letter?", ["It contains a complete explanation of the later deaths", "It was written only to invite Kogoro to the memorial service", "It proves that reports of the pianist's death were false", "Its impossible-looking sender makes the request itself something to investigate"], 4,
          "正解は4。依頼を成立させる手紙であると同時に、『亡くなった人物が依頼人』という矛盾そのものが手がかりになる。3のように死亡情報が誤りだと証明したわけではない。"),
        q(28, "What role does the Moonlight Sonata play in the second paragraph?", ["It shows that everyone at the memorial knew the dead pianist personally", "It links the present event to the older death without proving who caused the music", "It makes the letter unnecessary because the melody gives the full answer", "It proves that the current mayor selected the music for the service"], 2,
          "正解は2。曲は過去と現在を結び付けるが、誰が流したかは確定しない。1・4は本文にない。3は『複数の手がかりを比較する』という本文の論理に反する。"),
        q(29, "How is the blood-written score different from the earlier music?", ["It can only be understood by people who attended the old death", "It removes the need to examine the letter", "It is a visible message that can be examined and compared with the earlier clues", "It shows that the melody was not important to the case"], 3,
          "正解は3。音は共有される出来事、楽譜は目で確認し解釈できるメッセージとして区別されている。2・4は他の手がかりとの比較を否定している。"),
        q(30, "Why does the final paragraph say the order of the clues matters?", ["It allows readers to ignore the first clue after a stronger clue appears", "It makes the case easier because every clue has the same meaning", "It prevents investigators from changing their ideas during the case", "Later clues can force an earlier explanation to be reconsidered"], 4,
          "正解は4。新しい証拠が加わるたびに、それまでの仮説を修正する必要があるという段落の中心。1・2・3はいずれも逆。"),
        q(31, "Which of the following best expresses the main point of the passage?", ["The mystery becomes meaningful because different clues must be interpreted together and ideas must be revised", "A musical clue is always more reliable than a written clue", "Knowing the episode in advance is the best way to solve the questions", "The letter, music, and score all provide exactly the same information"], 1,
          "正解は1。本文全体は、異なる種類の手がかりを照合し、新情報で仮説を更新する読解過程を説明している。2・4は『手がかりごとに強みと限界が異なる』に反し、3は本文のみで解く設計に反する。"),
    ],
    "translation": [
        "2021年版の『月光』事件は、一つの矛盾から始まります。コナン、蘭、小五郎のもとに、月影島へ来るよう求める手紙が届きますが、依頼人として書かれていたのは、12年前に亡くなったとされるピアニストでした。したがって、この手紙には二つの役割があります。一つは、一行を島へ向かわせる実際の依頼であること。もう一つは、状況の中にまだ分かっていないことがあると示す証拠であることです。新たな死亡事件が起きる前から、依頼そのものが、聞かされている情報を疑って調べる理由になっています。",
        "公民館では前の村長の法要が行われており、その最中に『月光』が流れ始めます。この選曲が重要なのは、亡くなったピアニストも同じ曲を弾きながら亡くなったとされているからです。このつながりによって、昔の出来事が現在の中で再び重要になります。ただし、曲を聞いたからといって、それを流した人物まで分かるわけではありません。この事件では、『つながりに気付くこと』と『原因を証明すること』の間に、あえてはっきりした距離が残されています。",
        "現職の村長が遺体で見つかると、状況はいっそう深刻になります。さらに、血で書かれた楽譜が発見され、コナンはそこからメッセージを読み取ります。この手がかりは、目で見て直接調べられる物である点で、先ほどの音楽とは異なります。手紙は『過去が戻ってきたのではないか』と思わせ、音楽は過去と現在を結び付け、楽譜は解釈できるメッセージを加えます。それぞれの手がかりには異なる強みと限界があるため、一つがほかを単純に不要にするわけではありません。",
        "この事件で注意深く読む必要がある理由の一つは、手がかりが現れる順番です。もし最後のメッセージが最初に示されていたなら、その前の手紙や音楽は、ただの飾りのように感じられたかもしれません。ところが実際には、後から加わる情報によって、それ以前の出来事の意味が変わっていきます。手紙を読んだ時点ではもっともらしく見えた説明も、音楽が流れれば修正が必要になり、楽譜が見つかればさらに考え直さなければなりません。つまり、このミステリーは、有名な曲の名前を知っているだけでは解けません。新しい証拠を、それまでの考えと何度も照らし合わせ、合わなくなれば考えを修正していくことで進んでいくのです。",
    ],
}

SETS.append(conan)

# -----------------------------------------------------------------------------
# SET 2: FULLMETAL ALCHEMIST — verified manga-series premise / Vol. 1
# -----------------------------------------------------------------------------
fma = {
    "slug": "fullmetal_alchemist_origin",
    "display_title": "FULLMETAL ALCHEMIST",
    "jp_title": "『鋼の錬金術師』― エルリック兄弟の出発点 Special Practice Set",
    "episode_label": "The Elric Brothers' Failed Alchemical Ritual and the Search for the Philosopher's Stone",
    "intro_jp": "『鋼の錬金術師』は、錬金術が存在する世界で、エドワードとアルフォンスの兄弟が失った身体を取り戻すために旅をする物語です。今回は、兄弟の錬金術が失敗し、その代償が後の旅の目的へつながっていく代表的な出発点を扱います。必要な作品情報は本文中で説明します。",
    "background_en": p("""
        Edward and Alphonse Elric use alchemy in an attempt to fulfill their dearest wish, but the ritual goes terribly wrong. Edward loses an arm and a leg, while Alphonse becomes a soul inside a suit of armor. Edward later uses mechanical auto-mail limbs and becomes a State Alchemist. The brothers begin searching for the legendary Philosopher's Stone because they hope it can help restore their bodies. This practice set focuses on the causal chain created by the failed ritual: a choice produces lasting physical consequences, those consequences create a new goal, and that goal sends the brothers into a much larger world of alchemy and conflict. The passages are original and can be solved without prior knowledge of the manga.
    """),
    "names": [
        ("エドワード・エルリック", "Edward Elric"),
        ("アルフォンス・エルリック", "Alphonse Elric"),
        ("賢者の石", "Philosopher's Stone"),
        ("国家錬金術師", "State Alchemist"),
        ("オートメイル", "auto-mail"),
    ],
    "source_note_internal": "VIZ official Fullmetal Alchemist series and Vol. 1 descriptions; fact verification only.",
}

fma["part1"] = [
    q(1, "The brothers hoped alchemy would ( ) their loss, but the ritual caused even greater damage.", ["divide", "announce", "reverse", "decorate"], 3, "正解は3 reverse「元に戻す、逆転させる」。失ったものを取り戻そうとする文脈。divideは「分ける」、announceは「発表する」、decorateは「飾る」。"),
    q(2, "Edward suffered a terrible ( ) when the ritual went wrong: he lost an arm and a leg.", ["consequence", "invitation", "bargain", "entrance"], 1, "正解は1 consequence「結果、重大な帰結」。失敗した錬金術の結果として身体を失う。invitationは「招待」、bargainは「取引」、entranceは「入口」。"),
    q(3, "Alphonse no longer had a normal body; his soul was ( ) to a suit of armor.", ["compared", "delivered", "invited", "bound"], 4, "正解は4 bound「結び付けられた」。魂が鎧の中にある状態に合う。comparedは「比較された」、deliveredは「届けられた」、invitedは「招かれた」。"),
    q(4, "Edward later used ( ) auto-mail limbs, which allowed him to move despite his injuries.", ["distant", "mechanical", "common", "empty"], 2, "正解は2 mechanical「機械の」。auto-mailは機械式の義肢として説明される。distantは「遠い」、commonは「一般的な」、emptyは「空の」。"),
    q(5, "Their search for the Philosopher's Stone had a clear ( ): to restore their bodies.", ["purpose", "surface", "custom", "border"], 1, "正解は1 purpose「目的」。to restore their bodies が目的を説明している。surfaceは「表面」、customは「習慣」、borderは「境界」。"),
    q(6, "The failed ritual taught the brothers that powerful actions can have ( ) results.", ["polite", "equal", "serious", "narrow"], 3, "正解は3 serious「重大な」。身体を失うほどの結果に合う。politeは「礼儀正しい」、equalは「等しい」、narrowは「狭い」。"),
    q(7, "Edward became a State Alchemist, giving him a position inside the ( ) system.", ["musical", "military", "medical", "farming"], 2, "正解は2 military「軍の」。公式英語版の説明でもEdwardは政府・軍の錬金術師として扱われる。musicalは「音楽の」、medicalは「医療の」、farmingは「農業の」。"),
    q(8, "Even after the loss, the brothers remained ( ) to find a way forward.", ["rare", "silent", "ordinary", "determined"], 4, "正解は4 determined「決意して」。失った身体を取り戻す道を探し続ける姿勢。rareは「珍しい」、silentは「静かな」、ordinaryは「普通の」。"),
    q(9, "The Philosopher's Stone is valuable to them because they believe it may help ( ) their bodies.", ["borrow", "divide", "restore", "mail"], 3, "正解は3 restore「元に戻す、回復させる」。兄弟の目的に一致する。borrowは「借りる」、divideは「分ける」、mailは「郵送する」。"),
    q(10, "The brothers' goal is personal, but their journey brings them into ( ) with dangerous enemies.", ["conflict", "profit", "ceremony", "weather"], 1, "正解は1 conflict「対立、争い」。危険な敵とぶつかる文脈。profitは「利益」、ceremonyは「式典」、weatherは「天気」。"),
    q(11, "Edward became a State Alchemist partly ( ) information and opportunities that might help the search.", ["by mistake", "in search of", "at first sight", "on the contrary"], 2, "正解は2 in search of「～を求めて」。情報や機会を求めるという意味。by mistakeは「誤って」、at first sightは「一見して」、on the contraryは「それどころか」。"),
    q(12, "The brothers had to ( ) the results of the decision they made when they were younger.", ["run into", "call off", "hand out", "deal with"], 4, "正解は4 deal with「～に対処する」。過去の決断が生んだ結果に向き合う。run intoは「偶然会う」、call offは「中止する」、hand outは「配る」。"),
    q(13, "The story makes clear that trying to change nature can ( ) a high cost.", ["come at", "grow into", "look after", "turn down"], 1, "正解は1 come at a high cost「大きな代償を伴う」。grow intoは「成長して～になる」、look afterは「世話をする」、turn downは「断る／音量を下げる」。"),
    q(14, "Edward's mechanical limbs help him move, but they do not ( ) what happened.", ["put away", "stand for", "take off", "make up for"], 4, "正解は4 make up for「～を埋め合わせる」。義肢は動けるようにするが、起きたこと自体を帳消しにはしない。put awayは「片付ける」、stand forは「～を表す」、take offは「脱ぐ／離陸する」。"),
    q(15, "After the ritual failed, the brothers ( ) to find the Philosopher's Stone.", ["settled for", "ran out of", "set out", "fell behind"], 3, "正解は3 set out「出発する、取りかかる」。石を探す旅へ向かう。settle forは「～で妥協する」、run out ofは「～を使い果たす」、fall behindは「遅れる」。"),
    q(16, "Edward had to ( ) his new role while still pursuing his personal goal.", ["break down", "take on", "turn over", "pass by"], 2, "正解は2 take on「役割・責任を引き受ける」。State Alchemistという新しい立場を引き受ける。break downは「故障する」、turn overは「ひっくり返す」、pass byは「通り過ぎる」。"),
    q(17, "One decision can ( ) consequences that continue for years.", ["look into", "give away", "call on", "lead to"], 4, "正解は4 lead to「～につながる」。一つの決断が長期的な結果につながる。look intoは「調べる」、give awayは「無料で与える／秘密を漏らす」、call onは「訪ねる／求める」。"),
]

fma["part2a"] = {
    "title": "A Wish with a Cost",
    "paragraphs": [
        p("""Edward and Alphonse Elric are talented young brothers who believe strongly in the power of alchemy. They use it in an attempt to fulfill their dearest wish, but the ritual goes terribly wrong. The event does not simply fail to give them what they wanted. It takes something from them. Edward loses an arm and a leg, while Alphonse loses his normal body and becomes a soul inside a suit of armor. In other words, ( 18 )."""),
        p("""The damage changes the brothers' lives in different ways. Edward later uses mechanical auto-mail limbs, which allow him to move and continue acting in the world. Alphonse can also continue traveling, but his condition is very different because he no longer has an ordinary human body. These solutions keep the brothers moving, yet they do not erase the loss. ( 19 ). Their next major goal is therefore not to repeat the original ritual but to find a way to restore what was lost."""),
        p("""That goal gives the story a new direction. Edward becomes a State Alchemist, and the brothers begin searching for the legendary Philosopher's Stone. They hope its power may help them recover their bodies. The stone is important not because the brothers simply want a valuable object, but because it is connected to a problem created by their own earlier choice. ( 20 ), the failed ritual becomes more than a painful memory: it becomes the cause of the journey that follows."""),
    ],
    "questions": [
        q(18, "", ["the ritual gives both brothers stronger bodies than before", "the brothers decide to stop using alchemy forever", "the result is the opposite of the restoration they hoped to achieve", "the experiment succeeds but attracts dangerous enemies"], 3, "正解は3。願いをかなえるための錬金術が、逆に身体を失わせたという因果をまとめている。1・4は結果が成功したことにしており、2は本文にない。"),
        q(19, "", ["The lasting damage is the reason they begin to seek restoration", "Edward's auto-mail completely solves every problem caused by the ritual", "Alphonse immediately returns to a normal human body", "The brothers decide that physical recovery is no longer important"], 1, "正解は1。義肢や鎧で行動は続けられるが、損失自体は残るため、回復が次の目標になる。2・3は事実と反し、4は逆。"),
        q(20, "", ["On the other hand", "Because of this", "For instance", "At first"], 2, "正解は2 Because of this「このため」。失敗による問題が、後の旅の原因になるという明確な因果関係。"),
    ],
    "translation": [
        "エドワードとアルフォンス・エルリックは、錬金術の力を強く信じている才能ある若い兄弟です。2人は、どうしてもかなえたい願いのために錬金術を使いますが、その試みはひどい失敗に終わります。ただ願いがかなわなかっただけではありません。代わりに、兄弟自身が大切なものを失います。エドワードは片腕と片脚を失い、アルフォンスは普通の身体を失って、鎧の中の魂だけの存在になります。つまり、取り戻そうとして行った錬金術が、期待とは逆に、2人から身体を奪う結果になったのです。",
        "その損失は、兄弟の生活をそれぞれ違う形で変えます。エドワードは後に機械式のオートメイルの義肢を使い、それによって動き、行動を続けることができます。アルフォンスも旅を続けられますが、普通の人間の身体を持っていないため、置かれている状況は大きく異なります。こうした手段によって2人は前へ進めるものの、失ったものが消えるわけではありません。その損失が残り続けるからこそ、兄弟は身体を取り戻す方法を探し始めます。したがって次の大きな目標は、最初の試みをやり直すことではなく、失ったものを回復する方法を見つけることになります。",
        "その目標によって、物語は新しい方向へ進みます。エドワードは国家錬金術師となり、兄弟は伝説の『賢者の石』を探し始めます。その力なら、自分たちの身体を取り戻す助けになるかもしれないと考えるからです。石が重要なのは、兄弟が単に価値の高い物を欲しがっているからではありません。自分たちの過去の選択が生み出した問題を解決する手段として、石が必要なのです。このため、失敗した錬金術は、ただのつらい思い出ではなく、その後の旅そのものを生み出す原因になります。",
    ],
}

fma["part2b"] = {
    "title": "More Than a Treasure",
    "paragraphs": [
        p("""The Philosopher's Stone might look like a typical fantasy treasure, but it has a special meaning for Edward and Alphonse. They are not searching for it mainly because it is rare, famous, or valuable. The brothers lost parts of their bodies in a failed alchemical ritual, and they hope the stone can help restore them. For that reason, ( 21 ). The object matters because it is tied directly to damage the brothers are trying to undo."""),
        p("""Edward's position as a State Alchemist also changes the nature of the search. He is no longer only a boy looking for a private solution. He has entered a government and military system in which alchemy has wider uses and consequences. His position can give him opportunities to follow information, but it also places his personal goal inside a larger world of duties, power, and other alchemists. ( 22 )."""),
        p("""This makes the search more complicated than a simple trip toward one valuable object. The brothers' goal remains clear, yet each new place or person can force them to think about the power they are trying to obtain and the price that may come with it. Their first mistake cannot be removed simply by pretending it never happened. ( 23 ), the search for the stone keeps returning them to the question of how to repair the results of an earlier choice without creating another harmful result."""),
    ],
    "questions": [
        q(21, "", ["the brothers want the stone mainly to become rich", "the stone is valuable only because the military wants it", "the brothers can recover without changing anything about their lives", "the stone's value comes from its possible connection to restoring their bodies"], 4, "正解は4。石の価値は希少性や金銭ではなく、失った身体を取り戻す可能性に直接結び付いている。1・2は目的のすり替え、3は損失を無視している。"),
        q(22, "", ["His personal search therefore becomes connected with a much larger social system", "His government role prevents him from learning anything about alchemy", "The brothers stop caring about their own bodies after he receives the title", "Only military officers are allowed to know that the Philosopher's Stone exists"], 1, "正解は1。State Alchemistになることで、個人的な目的が政府・軍・他の錬金術師が関わる広い世界とつながる。2・3・4は本文にない。"),
        q(23, "", ["In comparison", "At random", "For this reason", "On average"], 3, "正解は3 For this reason「このため」。最初の失敗が消えないからこそ、石を探す旅でも『どう修復するか』という問題が繰り返し現れる。"),
    ],
    "translation": [
        "『賢者の石』は、よくあるファンタジーの宝物のようにも見えます。しかし、エドワードとアルフォンスにとっては特別な意味があります。2人が石を探している主な理由は、珍しいからでも、有名だからでも、高価だからでもありません。兄弟は失敗した錬金術で身体の一部を失い、石の力ならそれを取り戻す助けになるかもしれないと考えています。そのため、石の価値は、兄弟が身体を回復できるかもしれないという可能性と結び付いています。この物が重要なのは、2人が元に戻そうとしている損失に直接関係しているからです。",
        "エドワードが国家錬金術師になったことも、探索の性質を変えます。彼はもう、個人的な解決策を探すだけの少年ではありません。錬金術がより広い目的に使われ、より大きな影響を持つ政府や軍の仕組みの中へ入ったのです。その立場によって情報を追う機会が得られる一方で、彼の個人的な目的は、任務や権力、ほかの錬金術師たちが関わる大きな世界の中に置かれます。こうして、エドワード個人の探索は、はるかに大きな社会の仕組みと結び付いていきます。",
        "その結果、探索は、一つの価値ある物を目指して進む単純な旅ではなくなります。兄弟の目的自体は明確ですが、新しい場所や人物に出会うたび、自分たちが手に入れようとしている力や、その力に伴うかもしれない代償について考えさせられることがあります。最初の失敗は、なかったことにして消せるものではありません。このため、賢者の石を探す旅では、過去の選択が生み出した結果を、別の害を生まずにどう修復するのかという問題が何度も戻ってくるのです。",
    ],
}

fma["part3a"] = {
    "headers": {
        "From": "Mika Tanaka <mika@eastsciencecenter.example>",
        "To": "Paul Grant <pgrant@riversidehs.example>",
        "Date": "September 11",
        "Subject": "Fullmetal Alchemist science-and-story workshop",
    },
    "greeting": "Dear Paul,",
    "paragraphs": [
        p("""Thank you for reserving places for your students in our science-and-story workshop. We use the beginning of Fullmetal Alchemist to discuss how a fictional experiment can create lasting consequences. The first station shows a simple model of Edward and Alphonse's goal and the damage caused by their failed ritual. The second uses a safe mechanical-limb model to introduce the idea of auto-mail. The third asks students to compare two possible routes for the brothers after the accident: giving up their goal or searching for a way to restore their bodies. No chemical experiment or dangerous demonstration is included."""),
        p("""Your group is booked for the 10:00 a.m. session. Please arrive fifteen minutes early. Students will work in pairs, so an even number is helpful but not required. We provide worksheets and pencils. The mechanical model is handled only by museum staff because one joint can be damaged if it is bent too far."""),
        p("""Before the visit, please tell students that this is a reading activity, not a quiz about the series. They should use the information on each station card. We especially want them to notice that the Philosopher's Stone matters because of the brothers' earlier loss, not simply because it is a rare treasure."""),
    ],
    "closing": "Sincerely,\nMika Tanaka\nEast Science Center",
    "questions": [
        q(24, "What is one purpose of the workshop's first station?", ["To teach students how to perform alchemy safely", "To show the connection between the brothers' goal and the damage caused by the failed ritual", "To let students build a real auto-mail limb", "To compare several different anime series"], 2, "正解は2。第1ステーションは兄弟の目的と失敗の結果を結び付ける。1は危険実験を行わないことに反し、3は第2ステーションかつスタッフのみ、4は記載なし。"),
        q(25, "What does Mika say about the mechanical model?", ["Students must bring their own tools to repair it", "It will be removed if an odd number of students attends", "Students may take it apart after the workshop", "Only museum staff should handle it because it can be damaged"], 4, "正解は4。関節を曲げすぎると壊れる可能性があるのでスタッフだけが扱う。1・2・3は本文にない。"),
        q(26, "What should students understand about the Philosopher's Stone before the visit?", ["It is valuable mainly because the military wants to sell it", "Its importance comes from the brothers' effort to recover from an earlier loss", "It appears only in the science center's original story", "It is used in the workshop as a real chemical material"], 2, "正解は2。希少な宝だからではなく、兄弟の以前の損失を取り戻す目的と結び付く点を理解してほしいとある。"),
    ],
    "translation": [
        "ポールへ\n\n本センターの『科学と物語』ワークショップに生徒のみなさんの席を予約してくださり、ありがとうございます。私たちは『鋼の錬金術師』の物語の出発点を使い、架空の実験が長く残る結果を生むことについて考えます。第1ステーションでは、エドワードとアルフォンスの目的と、失敗した錬金術によって生じた損失を簡単な模型で示します。第2ステーションでは、安全な機械式義肢の模型を使ってオートメイルという考え方を紹介します。第3ステーションでは、事故の後で兄弟が取れた二つの道、つまり目標をあきらめる道と、身体を取り戻す方法を探す道とを比較します。化学実験や危険な実演は行いません。",
        "みなさんのグループは午前10時の回に予約されています。15分前までに来てください。生徒は2人組で活動するので偶数人数だと進めやすいですが、必須ではありません。ワークシートと鉛筆はこちらで用意します。機械式義肢の模型は、一つの関節を曲げすぎると壊れる可能性があるため、博物館スタッフだけが扱います。",
        "来館前に、この活動は作品知識を競うクイズではなく、英文を読む活動だと生徒に伝えてください。各ステーションのカードに書かれている情報を使って考えるようにしてください。特に、『賢者の石』が重要なのは単に珍しい宝物だからではなく、兄弟が以前に失ったものと結び付いているからだという点に気付いてほしいと思っています。\n\nよろしくお願いします。\n田中美香\nイースト・サイエンス・センター",
    ],
}

fma["part3b"] = {
    "title": "The Story Begins After the Mistake",
    "paragraphs": [
        p("""Many adventure stories begin with a hero who wants something and then leaves home to get it. Fullmetal Alchemist starts from a more difficult position. Before Edward and Alphonse begin their search for the Philosopher's Stone, they have already made a decision that changed their bodies. Their alchemical ritual goes wrong: Edward loses an arm and a leg, while Alphonse becomes a soul inside a suit of armor. The later journey is therefore shaped by consequences that are already present from the beginning."""),
        p("""The brothers find ways to continue living, but those solutions do not remove the central problem. Edward uses mechanical auto-mail limbs, which allow him to move and work despite what he lost. Alphonse can also travel and act, but he does so without an ordinary human body. These conditions are useful for continuing the journey, yet they also keep the earlier failure visible. Each brother can move forward, but neither can simply return to the life he had before the ritual."""),
        p("""Edward then becomes a State Alchemist, and the brothers search for the Philosopher's Stone in the hope of restoring their bodies. His new position places a personal goal inside a much larger government and military world. The brothers also encounter other people who use alchemy for their own purposes. As a result, the question is no longer only whether the brothers can find a powerful object. Their private need for restoration becomes connected with a world in which power can be used in many different ways."""),
        p("""This causal chain gives the opening of the series much of its force. A failed attempt creates physical loss; the loss creates the need for restoration; that need produces the search for the Stone; and the search brings the brothers into larger conflicts. The first mistake is therefore not just background information that can be forgotten once the adventure begins. It continues to shape what the brothers want and why their choices matter. The journey moves forward because they are trying to repair an earlier action, not because the past has disappeared."""),
    ],
    "questions": [
        q(27, "What does the first paragraph say is unusual about the beginning of the story?", ["The brothers' search is driven by serious consequences that already exist before the journey starts", "Edward begins with the Philosopher's Stone already in his possession", "The brothers leave home before they have any goal at all", "Alchemy has not yet affected either brother when they begin traveling"], 1, "正解は1。旅に出る前にすでに身体的な代償を負っており、それが旅の動機になる。2・3・4は本文と反する。"),
        q(28, "What point does the second paragraph make about auto-mail and Alphonse's armor body?", ["They make the brothers stronger than every other alchemist", "They prove that the original ritual was actually successful", "They allow the brothers to continue while the results of their loss still remain", "They remove the brothers' need to restore their bodies"], 3, "正解は3。2人が行動を続ける助けにはなるが、以前の損失自体は消さない。2・4は段落の逆、1は比較自体がない。"),
        q(29, "How does Edward's position as a State Alchemist affect the story according to the third paragraph?", ["It connects the brothers' personal goal with a larger government and military world", "It ends their search because the military gives them the Stone", "It prevents them from meeting other people who use alchemy", "It makes restoring their bodies less important to them"], 1, "正解は1。個人的な回復の目標が、政府・軍・他の錬金術師が存在する広い世界と結び付く。2・3・4は本文にない。"),
        q(30, "Which sequence best matches the causal chain described in the final paragraph?", ["State title → body loss → failed ritual → search", "Search → body loss → successful ritual → peace", "Armor body → military order → forgotten past → treasure", "Failed ritual → physical loss → need for restoration → search for the Stone"], 4, "正解は4。最終段落に明示された因果の順序そのもの。ほかは順序や内容を入れ替えている。"),
        q(31, "Which of the following best expresses the main point of the passage?", ["The brothers can move forward only after they stop thinking about the past", "The initial failure is not just background; it creates the conditions and goals that shape the journey", "Edward's government job is more important than the brothers' wish to recover", "The story treats the Philosopher's Stone mainly as a symbol of wealth"], 2, "正解は2。失敗→損失→回復目標→探索という連鎖が物語を動かし続けるのが本文全体の主張。1・3・4は中心関係を取り違えている。"),
    ],
    "translation": [
        "多くの冒険物語は、主人公が何かを求め、それを手に入れるために旅立つところから始まります。しかし『鋼の錬金術師』は、もっと難しい状況から始まります。エドワードとアルフォンスが賢者の石を探し始める前に、2人はすでに、自分たちの身体を変えてしまう決断をしています。錬金術の試みが失敗し、エドワードは片腕と片脚を失い、アルフォンスは鎧の中の魂だけの存在になります。つまり、その後の旅は、物語の最初からすでに存在している『過去の選択の結果』によって形作られているのです。",
        "兄弟は生活を続ける方法を見つけますが、それで中心的な問題が消えるわけではありません。エドワードは機械式のオートメイルの義肢を使い、失ったものがあっても動き、行動できます。アルフォンスも旅をして行動できますが、普通の人間の身体を持たない状態です。こうした方法は旅を続けるうえでは役立ちますが、以前の失敗を見えなくしてくれるものではありません。2人とも前へ進むことはできても、錬金術を行う前の生活へそのまま戻ることはできないのです。",
        "その後、エドワードは国家錬金術師となり、兄弟は身体を取り戻すことを願って賢者の石を探します。エドワードの新しい立場によって、個人的な目標が、より大きな政府や軍の世界の中に置かれます。兄弟は、自分なりの目的で錬金術を使うほかの人々とも出会います。その結果、問題は単に『強い力を持つ物を見つけられるか』だけではなくなります。身体を取り戻したいという兄弟個人の必要が、力がさまざまな目的に使われる大きな世界と結び付いていくのです。",
        "この因果関係の連なりが、物語の出発点に強い意味を与えています。失敗した試みが身体の損失を生み、その損失が回復の必要を生み、その必要が賢者の石の探索へつながり、その探索が兄弟をより大きな対立へ導きます。したがって、最初の失敗は、冒険が始まれば忘れてよい単なる背景情報ではありません。兄弟が何を求めるのか、そしてなぜその選択が重要なのかを、ずっと形作り続けます。物語が前へ進むのは、過去が消えたからではなく、2人が過去の行動の結果を修復しようとしているからなのです。",
    ],
}

SETS.append(fma)

# -----------------------------------------------------------------------------
# SET 3: PRETTY GUARDIAN SAILOR MOON — 1992 TV anime Episode 1
# Verified against Toei Animation Episode 1 and VIZ Season 1 overview.
# -----------------------------------------------------------------------------
sailor = {
    "slug": "sailor_moon_episode1",
    "display_title": "PRETTY GUARDIAN SAILOR MOON",
    "jp_title": "『美少女戦士セーラームーン』第1話 Special Practice Set",
    "episode_label": "Episode 1: Usagi's First Transformation",
    "intro_jp": "『美少女戦士セーラームーン』は、普通の中学生・月野うさぎが、黒猫ルナとの出会いをきっかけにセーラー戦士として歩み始める作品です。今回は、うさぎがルナを助け、変身ブローチを受け取り、初めて新しい役割に向き合う第1話を題材にします。本文だけで解答できるよう必要な背景を説明しています。",
    "background_en": p("""
        Usagi Tsukino is an ordinary fourteen-year-old schoolgirl when she meets Luna, a black cat marked with a crescent moon. Usagi first helps the cat when some children are bothering her. Later, Luna comes to Usagi and gives her a special brooch that allows her to transform into Sailor Moon. Luna explains that Usagi has a mission connected with finding the Moon Princess and other Guardians. The new responsibility becomes immediate when Usagi hears her friend calling for help. This practice set uses the sequence of those verified events to build original reading questions about cause, timing, choice, and responsibility. Students do not need to know the series in advance; all information needed to answer the questions appears in the passages.
    """),
    "names": [
        ("月野うさぎ", "Usagi Tsukino"),
        ("ルナ", "Luna"),
        ("セーラームーン", "Sailor Moon"),
        ("変身ブローチ", "magic brooch"),
        ("月のプリンセス", "Moon Princess"),
    ],
    "source_note_internal": "Toei Animation 1992 TV Episode 1 description and VIZ Season 1 overview; fact verification only.",
}

sailor["part1"] = [
    q(1, "On her way to school, Usagi saw some children bothering a black cat and decided to ( ) it.", ["ignore", "frighten", "follow", "rescue"], 4, "正解は4 rescue「助ける」。困っている黒猫を助ける文脈。ignoreは「無視する」、frightenは「怖がらせる」、followは「後をついて行く」。"),
    q(2, "The cat Luna later ( ) Usagi a special brooch.", ["hid", "gave", "borrowed", "threw"], 2, "正解は2 gave「与えた」。Lunaがブローチを渡す出来事に合う。hidは「隠した」、borrowedは「借りた」、threwは「投げた」。"),
    q(3, "The brooch allowed Usagi to ( ) into Sailor Moon.", ["disappear", "compete", "transform", "graduate"], 3, "正解は3 transform「変身する」。broochによってSailor Moonに変身する。disappearは「消える」、competeは「競う」、graduateは「卒業する」。"),
    q(4, "Luna explained that Usagi had a ( ) to find the Moon Princess.", ["mission", "budget", "receipt", "habit"], 1, "正解は1 mission「使命、任務」。Moon Princessを探す役割の説明。budgetは「予算」、receiptは「領収書」、habitは「習慣」。"),
    q(5, "At first Usagi was an ( ) schoolgirl with everyday worries, which makes the change in her life feel sudden.", ["ancient", "formal", "private", "ordinary"], 4, "正解は4 ordinary「普通の」。日常生活を送る中学生という文脈。ancientは「古代の」、formalは「正式な」、privateは「私的な」。"),
    q(6, "When Usagi heard her friend crying for help, she had to act ( ).", ["immediately", "rarely", "softly", "equally"], 1, "正解は1 immediately「すぐに」。助けを求める声に応じる緊急性がある。rarelyは「めったに～ない」、softlyは「静かに」、equallyは「同等に」。"),
    q(7, "Luna's explanation helped Usagi ( ) why the brooch was important.", ["refuse", "understand", "damage", "replace"], 2, "正解は2 understand「理解する」。ブローチと新しい役割の意味を知る。refuseは「拒む」、damageは「傷つける」、replaceは「取り替える」。"),
    q(8, "The first episode moves quickly from daily life to a dangerous ( ).", ["discount", "harvest", "situation", "schedule"], 3, "正解は3 situation「状況」。日常から危険な状況へ移る。discountは「割引」、harvestは「収穫」、scheduleは「予定」。"),
    q(9, "Usagi had not planned to become a hero, so the new role came as a ( ).", ["surprise", "payment", "border", "method"], 1, "正解は1 surprise「驚き」。予想していなかった役割という文脈。paymentは「支払い」、borderは「境界」、methodは「方法」。"),
    q(10, "Her first decision to help Luna shows that she can be ( ) even before she has special powers.", ["silent", "wealthy", "careless", "kind"], 4, "正解は4 kind「親切な」。力を得る前から猫を助ける行動に合う。silentは「静かな」、wealthyは「裕福な」、carelessは「不注意な」。"),
    q(11, "Usagi ( ) Luna on her way to school before she understood who the cat was.", ["ran out of", "came across", "put off", "settled for"], 2, "正解は2 came across「偶然出会った」。通学途中の出会い。run out ofは「～を使い果たす」、put offは「延期する」、settle forは「～で妥協する」。"),
    q(12, "Her friend's cry for help made Usagi ( ) and use her new power.", ["put the task off", "turn the request down", "take action", "run out of time"], 3, "正解は3 take action「行動を起こす」。助けを求める声を聞き、新しい力を使う流れ。put offは「延期する」、turn downは「断る」、run out of timeは「時間がなくなる」。"),
    q(13, "By becoming Sailor Moon, Usagi begins to ( ) a responsibility she did not have that morning.", ["get rid of", "look down on", "come down with", "take on"], 4, "正解は4 take on「責任・役割を引き受ける」。新しい使命を担う。get rid ofは「取り除く」、look down onは「見下す」、come down withは「病気にかかる」。"),
    q(14, "The episode shows how an ordinary event can ( ) something much larger.", ["lead to", "pass by", "fall behind", "turn down"], 1, "正解は1 lead to「～につながる」。猫を助ける日常的な出来事が大きな変化へつながる。pass byは「通り過ぎる」、fall behindは「遅れる」、turn downは「断る」。"),
    q(15, "Luna tells Usagi to ( ) the Moon Princess and other Guardians.", ["put away", "look for", "give up", "take after"], 2, "正解は2 look for「～を探す」。使命の内容に合う。put awayは「片付ける」、give upは「あきらめる」、take afterは「～に似る」。"),
    q(16, "Even after receiving the brooch, Usagi must ( ) about whether to respond when someone needs help.", ["take part in", "get along with", "look forward to", "make up her mind"], 4, "正解は4 make up her mind「決心する」。力を持っただけでなく行動する決断が必要。take part inは「参加する」、get along withは「～とうまくやる」、look forward toは「楽しみにする」。"),
    q(17, "The first episode begins with a small act of kindness that later ( ) a much larger change in Usagi's life.", ["takes after", "turns down", "leads to", "runs into"], 3, "正解は3 leads to「～につながる」。小さな親切が大きな変化への出発点になる。take afterは「似る」、turn downは「断る」、run intoは「偶然会う／ぶつかる」。"),
]

sailor["part2a"] = {
    "title": "Before the Transformation",
    "paragraphs": [
        p("""At the beginning of the first Sailor Moon episode, Usagi Tsukino is still living an ordinary school life. On her way to school, she sees some children bothering a black cat with a crescent-moon mark on its forehead. Usagi stops and helps the cat. At that moment, she does not know that the cat is Luna or that the meeting will change her life. This is important because ( 18 )."""),
        p("""Later, Luna comes to Usagi and reveals that she can speak. She gives Usagi a special brooch, which allows her to transform into Sailor Moon. Luna also explains that Usagi has a new mission connected with finding the Moon Princess and other Guardians. The earlier meeting now has a different meaning because ( 19 ). What first looked like a small event on the way to school becomes the beginning of a much larger responsibility."""),
        p("""Usagi does not have much time to think about the new role in a calm way. Soon she hears her friend calling for help. The mission is no longer only something Luna has explained; it has become connected to a real person who needs help at that moment. Usagi must decide whether to use the power she has just received. ( 20 ), the episode moves from an ordinary act of kindness to the first test of a new responsibility."""),
    ],
    "questions": [
        q(18, "", ["Usagi already knows that Luna can give her special powers", "Usagi helps the cat before she expects any reward or heroic role", "the children tell Usagi where to find the Moon Princess", "Luna has already explained the full mission at school"], 2, "正解は2。うさぎは能力や使命を知る前に猫を助けている。1・3・4は出来事の順序を逆転・捏造している。"),
        q(19, "", ["the cat is not only an animal Usagi happened to meet but the one who brings her the brooch and mission", "Usagi learns that the children were secretly Guardians", "Luna asks Usagi to return the brooch immediately", "the meeting proves that Usagi had planned to become Sailor Moon"], 1, "正解は1。後の情報によって最初の出会いの意味が変わる。2・3・4はいずれも本文にない。"),
        q(20, "", ["On average", "In the past", "For example", "As a result"], 4, "正解は4 As a result「その結果」。友人の助けを求める声によって、説明された使命が実際の行動へ移るという結果を示す。"),
    ],
    "translation": [
        "『セーラームーン』第1話の冒頭で、月野うさぎはまだ普通の学校生活を送っています。学校へ向かう途中、額に三日月の模様がある黒猫が子どもたちに困らされているのを見つけ、うさぎは立ち止まって猫を助けます。その時点では、その猫がルナだということも、この出会いが自分の人生を変えることも知りません。ここが大切なのは、うさぎが何か特別な力やヒーローとしての役割を期待する前に、猫を助けているからです。",
        "その後、ルナはうさぎのもとへやって来て、人間の言葉を話せることを明かします。そして、うさぎに特別なブローチを渡します。そのブローチによって、うさぎはセーラームーンへ変身できます。さらにルナは、月のプリンセスや仲間の戦士を探すことに関わる新しい使命を説明します。ここで最初の出会いの意味が変わります。あの猫は、たまたま出会った動物ではなく、うさぎにブローチと使命をもたらす存在だったからです。登校途中の小さな出来事に見えたものが、より大きな責任の始まりになります。",
        "うさぎには、その新しい役割について落ち着いて考える時間がほとんどありません。やがて、友人が助けを求める声を聞きます。使命はもう、ルナから説明されただけの抽象的な話ではありません。今まさに助けを必要としている実際の人と結び付いたのです。うさぎは、受け取ったばかりの力を使うかどうか決めなければなりません。その結果、第1話は、日常の小さな親切から、新しい責任が初めて試される場面へと進んでいきます。",
    ],
}

sailor["part2b"] = {
    "title": "A Brooch and a New Role",
    "paragraphs": [
        p("""The brooch Luna gives Usagi is a small object, but it creates a clear change in what Usagi can do. Before receiving it, Usagi is an ordinary student who has helped a cat on the street. With the brooch, she can transform into Sailor Moon. The object therefore connects two sides of the same person: her daily life and her new identity as a Guardian. In practical terms, ( 21 )."""),
        p("""Yet a new ability is not the same thing as a complete plan. Luna also tells Usagi that she has a mission involving the Moon Princess and other Guardians. This information gives a direction to the power represented by the brooch. ( 22 ). Usagi still needs to understand situations and decide when her new ability should be used. The object makes action possible, while the mission explains why action may be necessary."""),
        p("""The first episode tests this difference almost immediately. Usagi hears her friend calling for help, so the new role becomes connected to an urgent problem instead of remaining only an explanation from Luna. She now has both the ability to transform and a reason to act. ( 23 ), the importance of the brooch becomes clearest not when it is simply given to Usagi, but when she must choose to use the power it provides."""),
    ],
    "questions": [
        q(21, "", ["the brooch makes Usagi forget her ordinary life", "the brooch automatically solves every danger near Usagi", "the brooch gives Usagi a clear way to enter her new identity and act", "the brooch tells Usagi the location of every Guardian"], 3, "正解は3。ブローチは日常のうさぎとセーラームーンという新しい役割を、具体的な『変身する行動』で結び付ける。1・2・4は本文にない。"),
        q(22, "", ["The mission proves that Usagi no longer needs the brooch", "Power alone does not tell Usagi what she should do with it", "Luna asks Usagi to avoid helping people until every Guardian is found", "Usagi already knows every detail of the mission before meeting Luna"], 2, "正解は2。能力そのものと、その能力を何のために使うかという方向性は別だという段落の中心。1・3・4は逆または本文にない。"),
        q(23, "", ["For this reason", "On the contrary", "At first", "By chance"], 1, "正解は1 For this reason「このため」。能力と緊急の理由がそろうため、実際に使う選択の場面でブローチの意味が明確になる。"),
    ],
    "translation": [
        "ルナがうさぎに渡すブローチは小さな物ですが、うさぎに『できること』をはっきり変えます。受け取る前のうさぎは、道で猫を助けた普通の生徒です。しかしブローチを使えば、セーラームーンへ変身できます。そのため、この物は、うさぎという一人の人間の二つの面、つまり日常生活を送る姿と、戦士としての新しい姿を結び付けます。具体的には、ブローチによって、うさぎは新しい役割へ移り、実際に行動するための明確な方法を得るのです。",
        "ただし、新しい能力を持つことと、何をすべきかがすべて決まっていることは同じではありません。ルナは、月のプリンセスやほかの戦士に関わる使命も伝えます。この情報によって、ブローチが表す力に方向性が与えられます。力を持っているだけでは、その力を何のために使うべきかまでは分かりません。うさぎ自身が状況を理解し、新しい能力をいつ使うべきか判断する必要があります。ブローチは行動を可能にし、使命はなぜ行動が必要なのかを示すのです。",
        "第1話では、この違いがほとんどすぐに試されます。うさぎが友人の助けを求める声を聞いたことで、新しい役割は、ルナの説明だけにとどまらず、緊急の問題と結び付きます。これで、うさぎには変身する能力と、行動する理由の両方がそろいます。このため、ブローチの重要性が最もはっきりするのは、ただ渡された瞬間ではなく、うさぎが、その力を実際に使うかどうか選ばなければならない場面なのです。",
    ],
}

sailor["part3a"] = {
    "headers": {
        "From": "Yumi Hayashi <yumi@harborhs.example>",
        "To": "Ken Martin <kmartin@harborhs.example>",
        "Date": "September 11",
        "Subject": "Sailor Moon story-sequence booth",
    },
    "greeting": "Hi Ken,",
    "paragraphs": [
        p("""Thanks for helping with our school festival booth about the first Sailor Moon episode. Visitors will work with three short story cards. Card A describes Usagi helping Luna before she knows anything about special powers. Card B explains that Luna later gives Usagi a magic brooch and tells her about a new mission. Card C describes Usagi hearing a friend call for help. Teams must put the cards in the correct order and then explain how each event changes the meaning of the previous one."""),
        p("""Please place Card A at the entrance, but keep Cards B and C face down until each team is ready. In yesterday's test, some visitors read Card C first and immediately treated the booth as a simple battle story. We want them to notice the change from ordinary life to responsibility. Each team will have eight minutes, and no phones are needed."""),
        p("""Could you also prepare ten pencils and five clipboards? We already printed the cards, so please do not make new copies. If a visitor knows the episode well, remind them that the explanation must be based on the English cards rather than on details they remember from the anime."""),
    ],
    "closing": "Thanks,\nYumi",
    "questions": [
        q(24, "What do visitors have to do at the booth?", ["Draw a new Sailor Moon costume", "Watch the whole first episode on a phone", "Choose which card has the best artwork", "Arrange the story cards and explain the relationship among the events"], 4, "正解は4。カードを正しい順に並べ、各出来事が前の出来事の意味をどう変えるか説明する。1・2・3は本文にない。"),
        q(25, "Why should Cards B and C remain face down at first?", ["The cards have not been printed yet", "The teacher wants visitors to use their phones before reading", "Reading the later event too early can make visitors miss the change from ordinary life to responsibility", "The cards contain information that only teachers are allowed to see"], 3, "正解は3。Card Cを先に読むと単純な戦闘物語として捉えやすく、日常→責任の変化を見落とすため。1・2・4はメールに反する。"),
        q(26, "What should Ken tell visitors who already know the episode?", ["They may skip the English cards and answer from memory", "They should support their explanation with the information on the English cards", "They should explain extra anime details to other teams", "They must leave the booth before the eight minutes end"], 2, "正解は2。作品知識ではなく英文カードを根拠に説明するよう求めている。1・3は逆、4は記載なし。"),
    ],
    "translation": [
        "ケンへ\n\n学校祭で行う『セーラームーン』第1話のブースを手伝ってくれてありがとう。参加者には、3枚の短いストーリーカードを使って活動してもらいます。Card Aには、うさぎが特別な力のことを何も知らない段階でルナを助ける出来事が書かれています。Card Bでは、後にルナがうさぎへ魔法のブローチを渡し、新しい使命について説明します。Card Cには、うさぎが友人の助けを求める声を聞く場面があります。チームはカードを正しい順に並べた後、それぞれの出来事によって、その前の出来事の意味がどう変わるのかを説明します。",
        "Card Aは入口に置いてください。ただしCard BとCard Cは、各チームが準備できるまで裏返しておいてください。昨日の試行では、Card Cを先に読んだ参加者の中に、すぐ『単純な戦いの話』として受け取ってしまう人がいました。私たちは、普通の日常から責任へと移っていく変化に気付いてほしいのです。各チームの時間は8分です。携帯電話は必要ありません。",
        "それから、鉛筆10本とクリップボード5枚を用意してもらえますか。カードはこちらですでに印刷してあるので、新しくコピーする必要はありません。もしエピソードをよく知っている参加者がいたら、アニメの記憶にある細かな情報ではなく、英語カードに書かれた情報を根拠に説明するよう伝えてください。\n\nありがとう。\n由美",
    ],
}

sailor["part3b"] = {
    "title": "From an Ordinary Morning to a Heroic Choice",
    "paragraphs": [
        p("""The first Sailor Moon episode begins by presenting Usagi Tsukino as an ordinary schoolgirl rather than as an experienced hero. On her way to school, she notices children bothering a black cat and decides to help it. At that time, she does not know the cat is Luna, and she has not received any special power. The action is small compared with what happens later, but it is important because Usagi makes a helpful choice before anyone tells her that she has a heroic role."""),
        p("""Later, Luna comes to Usagi and gives her a magic brooch that allows her to transform into Sailor Moon. Luna also explains that Usagi has a mission involving the Moon Princess and other Guardians. This is a major change in Usagi's situation. However, receiving power does not automatically decide every later action. The brooch changes what Usagi can do, while Luna's explanation changes what Usagi knows. Usagi herself still has to respond to the situations that follow."""),
        p("""That response is tested quickly when Usagi hears her friend calling for help. The new mission suddenly becomes connected with a person she knows rather than remaining a distant idea about a princess. The order of events is significant. First, Usagi helps without expecting a reward. Next, she learns that she has a new ability and responsibility. Then, someone actually needs her help. The episode can therefore be read as showing continuity between ordinary kindness and heroic action, instead of treating them as completely separate qualities."""),
        p("""This sequence also makes the transformation more meaningful. If Usagi had received the brooch before showing any concern for another person, her new identity could seem to come entirely from an outside object. Instead, the episode first shows a personal choice and only later adds the power to transform. The brooch is essential to becoming Sailor Moon, but it does not create every reason to act. Usagi's first day as a Guardian combines something new—special power and a mission—with something already visible in her ordinary life: the ability to notice someone in trouble and choose to help."""),
    ],
    "questions": [
        q(27, "What is important about Usagi helping Luna in the first paragraph?", ["She already knows Luna will give her a brooch", "She is following an order from another Guardian", "She expects the cat to reward her", "She makes a helpful choice before learning about any heroic role"], 4, "正解は4。能力や使命を知らない時点で助けていることが、後の行動とのつながりを作る。1・2・3は出来事の順序や動機を捏造している。"),
        q(28, "According to the second paragraph, what does the brooch change most directly?", ["What Usagi is able to do", "Who Usagi's friends are", "Where the Moon Princess is located", "What happened before Usagi met Luna"], 1, "正解は1。ブローチは『できること』、つまり変身能力を変える。一方、使命の説明は知識・方向性を変える。2・3・4は本文にない。"),
        q(29, "Why is the friend's call for help important in the third paragraph?", ["It proves that Usagi has already found every Guardian", "It makes Luna's mission unnecessary", "It turns the new responsibility from a distant idea into an immediate situation", "It shows that the first meeting with Luna was an accident with no later meaning"], 3, "正解は3。抽象的だった使命が『今、知っている人を助ける必要』と結び付く。1・2・4は本文の論理と反する。"),
        q(30, "What does the final paragraph suggest about the transformation?", ["The brooch is unimportant because Usagi was already kind", "The new power adds to a helpful quality that Usagi showed before becoming Sailor Moon", "Usagi becomes willing to help others only after receiving the brooch", "The mission is less important than ordinary school life"], 2, "正解は2。ブローチは必要だが、助けようとする性質はその前から見えている。1はブローチの重要性を否定し、3は順序が逆、4は比較していない。"),
        q(31, "Which of the following best expresses the main point of the passage?", ["The first episode connects Usagi's ordinary kindness with the new responsibility and power of Sailor Moon", "Usagi's ordinary life disappears completely as soon as Luna arrives", "The first episode is mainly about locating the Moon Princess immediately", "Knowing the ending of the series is necessary to understand Usagi's first transformation"], 1, "正解は1。本文全体は、普通の生活の中の親切と、新しい力・責任が連続して描かれることを説明している。2・3・4は本文の中心から外れる。"),
    ],
    "translation": [
        "『セーラームーン』第1話は、月野うさぎを、経験豊かなヒーローではなく普通の女子生徒として描くところから始まります。学校へ向かう途中、うさぎは子どもたちに困らされている黒猫に気付き、助けることを選びます。その時点では、猫がルナだということも、特別な力をもらうことも知りません。後で起こることに比べれば小さな行動ですが、ここには大切な意味があります。誰かから『あなたにはヒーローの役割がある』と言われる前に、うさぎ自身が人を助ける側の選択をしているからです。",
        "その後、ルナはうさぎのもとへ来て、セーラームーンへ変身できる魔法のブローチを渡します。また、月のプリンセスやほかの戦士に関わる使命があることも説明します。これは、うさぎの状況を大きく変える出来事です。ただし、力を得たからといって、その後のすべての行動が自動的に決まるわけではありません。ブローチは『うさぎに何ができるか』を変え、ルナの説明は『うさぎが何を知っているか』を変えます。しかし、その後の状況にどう応じるかは、うさぎ自身が決めなければなりません。",
        "その判断は、うさぎが友人の助けを求める声を聞いたことで、すぐに試されます。新しい使命は、遠いところにいるプリンセスについての抽象的な話ではなく、自分が知っている人と突然結び付きます。出来事の順番にも意味があります。最初に、うさぎは見返りを期待せずにルナを助けます。次に、新しい能力と責任があることを知ります。そして実際に、助けを必要とする人が現れます。そのため第1話は、日常の親切とヒーローとしての行動をまったく別の性質としてではなく、つながりのあるものとして描いている、と読むことができます。",
        "この順番によって、変身そのものにも大きな意味が生まれます。もし、うさぎが誰かを気にかける姿を一度も見せないままブローチを受け取っていたなら、新しい自分はすべて外から与えられた物によって生まれたように見えたかもしれません。しかし実際には、まず本人の選択が描かれ、その後で変身する力が加わります。セーラームーンになるうえでブローチは欠かせませんが、行動する理由のすべてをブローチが作るわけではありません。戦士としての最初の日には、特別な力と使命という新しいものと、普通の生活の中ですでに見えていたもの、つまり困っている相手に気付き、助けることを選ぶ力の両方が組み合わされているのです。",
    ],
}

SETS.append(sailor)

# Answer sequences are intentionally balanced according to the user's project rule
# (not claimed as an official Eiken rule). The material generator/auditor verifies them.

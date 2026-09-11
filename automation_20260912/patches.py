def apply_patches(sets):
    by_slug = {s['slug']: s for s in sets}

    s = by_slug['detective_conan_moonlight']
    s['part2b']['paragraphs'][1] += (
        " The timing also matters. A recording heard before a death would suggest something different "
        "from music heard only after investigators entered the room, so the sequence must be recorded carefully."
    )
    s['part2b']['translation'][1] += (
        " さらに、音が流れた時点も重要です。死亡事件より前に聞こえた録音と、捜査する人たちが部屋へ入った後にだけ聞こえた音楽とでは、示す意味が変わります。だからこそ、出来事の順序を丁寧に確認する必要があります。"
    )

    s = by_slug['fullmetal_alchemist_origin']
    s['part2b']['paragraphs'][1] += (
        " For example, information available through Edward's position may help the search, but following that "
        "information can also bring the brothers into conflicts that have little to do with wealth."
    )
    s['part2b']['translation'][1] += (
        " 例えば、エドワードの立場から得られる情報が探索の助けになる一方で、その情報を追うことで、金銭的な価値とはほとんど関係のない対立に兄弟が巻き込まれることもあります。"
    )

    s = by_slug['sailor_moon_episode1']
    s['part2a']['paragraphs'][0] += (
        " The episode does not begin by showing a chosen warrior in battle. It first shows a student responding "
        "to a small problem she notices during an ordinary morning."
    )
    s['part2a']['translation'][0] += (
        " この第1話は、選ばれた戦士がいきなり戦っている場面から始まるわけではありません。まず描かれるのは、普通の朝に目の前の小さな困り事へ反応する一人の生徒の姿です。"
    )
    s['part2b']['paragraphs'][1] += (
        " This distinction matters because tools and instructions play different roles. A tool can expand a person's "
        "options, while instructions can explain a goal without forcing the person to act."
    )
    s['part2b']['translation'][1] += (
        " この区別が大切なのは、道具と指示が果たす役割が異なるからです。道具は人が取れる行動の選択肢を増やせますが、指示は目的を示しても、その人に行動を強制するわけではありません。"
    )
    return sets

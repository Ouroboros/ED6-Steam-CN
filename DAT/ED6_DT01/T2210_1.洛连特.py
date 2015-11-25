from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_1838",         # 01, 1
        "Function_2_1874",         # 02, 2
        "Function_3_18B5",         # 03, 3
        "Function_4_18FB",         # 04, 4
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x10, 255)
    SetChrPos(0x101, 500, 0, 200, 0)
    SetChrPos(0x102, -500, 0, 200, 0)
    SetChrPos(0x105, 300, 0, -1300, 0)
    OP_6D(200, 0, 300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_235")
    Sleep(400)
    OP_8C(0x10, 180, 400)

    ChrTalk(
        0x10,
        (
            "#670FAh, you're here.\x02\x03",
            "Would you like to begin\x01",
            "your investigation?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_232")
    OP_0D()

    ChrTalk(
        0x101,
        "#003FSorry... Not just yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671FI see... Well, that's a shame,\x01",
            "but what's to be done?\x02\x03",
            "Once you have finished your\x01",
            "other business, please come\x01",
            "back to see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FGot it.\x02",
    )

    CloseMessageWindow()
    OP_28(0x20, 0x1, 0x2000)
    EventEnd(0x0)
    OP_4B(0x10, 255)
    OP_8C(0x10, 0, 0)
    Return()

    label("loc_232")

    Jump("loc_775")

    label("loc_235")


    ChrTalk(
        0x10,
        (
            "#673F...Oh, dear.\x02\x03",
            "I can't believe the Sapphire Glim\x01",
            "was stolen.\x02\x03",
            "#671FAnd why NOW, of all\x01",
            "possible times...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x10, 180, 400)
    Sleep(800)

    ChrTalk(
        0x10,
        (
            "#670FAh, you're here.\x02\x03",
            "I've been waiting for you\x01",
            "to show up.\x02\x03",
            "#672FHmm? Ah, Kloe's with you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x10, 400)

    ChrTalk(
        0x105,
        "#040FYes, I'm accompanying them.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_43C")
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe came as soon as we\x01",
            "saw the bulletin board.\x02\x03",
            "What seems to be the problem?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        "#671FAs you can see...\x02",
    )

    CloseMessageWindow()

    def lambda_3EB():
        OP_8C(0x102, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3EB)
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671FThis pedestal used to be adorned\x01",
            "with a candelabrum.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_43C")

    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#501FSorry for the hold-up...\x02\x03",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "#671FAs you can see...\x02",
    )

    CloseMessageWindow()

    def lambda_49F():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49F)
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671FThe candelabrum that once\x01",
            "stood atop this pedestal\x01",
            "has been stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044FOh, my...\x02",
    )

    CloseMessageWindow()

    label("loc_510")

    OP_28(0x20, 0x4, 0x2)

    ChrTalk(
        0x101,
        (
            "#004FAw, man...\x02\x03",
            "It really just disappeared\x01",
            "without a trace, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)

    ChrTalk(
        0x10,
        (
            "#671FThings being what they are,\x01",
            "I would like to ask you to\x01",
            "conduct a search.\x02\x03",
            "What say you? Are you available?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_775")
    OP_0D()

    ChrTalk(
        0x101,
        "#003FSorry, but we can't right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015FWe apologize.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671FNo, no need to apologize. I'm\x01",
            "sure that you have other work\x01",
            "to which you must attend.\x02\x03",
            "Once you have finished making\x01",
            "your arrangements, please come\x01",
            "back to see me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FNow, if you'll excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#670FYes, please.\x02",
    )

    CloseMessageWindow()
    OP_28(0x20, 0x1, 0x2000)
    EventEnd(0x0)
    OP_4B(0x10, 255)
    OP_8C(0x10, 0, 0)
    Return()

    label("loc_775")

    OP_28(0x20, 0x4, 0x8)
    OP_28(0x20, 0x4, 0x4)
    OP_28(0x20, 0x1, 0x1)
    OP_28(0x20, 0x1, 0x2)

    ChrTalk(
        0x101,
        "#006FFine with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#670FExcellent.\x02\x03",
            "Now, let me give you\x01",
            "some background...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)

    ChrTalk(
        0x10,
        (
            "#671FThe stolen item is a candelabrum\x01",
            "called the 'Sapphire Glim.'\x02\x03",
            "It is a fine piece of craftsmanship,\x01",
            "dating back to just after the\x01",
            "Orbal Revolution.\x02\x03",
            "A Dalmore family heirloom,\x01",
            "in fact.\x02\x03",
            "#673FIt would sell for hundreds of\x01",
            "thousands of mira, were it ever\x01",
            "placed on the open market.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x10, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FH-H-Hundreds of thousands of mira?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#013F...I see.\x02\x03",
            "It's probably not an issue\x01",
            "of petty burglary then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002FHuh? It's not?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015FYou'd have to have some\x01",
            "kind of safe way of laundering\x01",
            "something that valuable.\x02\x03",
            "So, whoever took it must be\x01",
            "well-connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FI get it...\x02\x03",
            "So that would rule out most\x01",
            "of your everyday thieves.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        (
            "#672FWell, actually...\x02\x03",
            "Money wasn't the primary\x01",
            "motivation for this crime,\x01",
            "it seems.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B22():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B22)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x101,
        "#004F...Huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#671FLook at this card.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'That which nests here is a beast more dire than\x01",
            "any other. Continue to give praise to the spirit\x01",
            "whose blue light was lost in the darkness. Free\x01",
            "the spark it left behind, and I will be free. Ahh,\x01",
            "seeker. The eyes of Aidios see only the truth,\x01",
            "and pass it on to you.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Look to the three-eyed giant which towers over\x01",
            "this settlement. Do so, and the blue light will be\x01",
            "revealed.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x102,
        "#012F...What's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671FA note left behind on the\x01",
            "bare pedestal.\x02\x03",
            "It appears to be written by\x01",
            "the thief himself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#002FHe wants us to know\x01",
            "he did it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "#671FSo I'm inclined to believe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FGot it. If all he was after\x01",
            "was money, this is a wee bit\x01",
            "excessive!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E6F():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E6F)
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#042FWhat he wrote must have\x01",
            "some significance.\x02\x03",
            "It almost sounds like\x01",
            "some kind of poetry.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#013FHmm...[blue light...lost in\x01",
            "the darkness...]\x02\x03",
            "I'm guessing the blue light refers\x01",
            "to the stolen candelabrum?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#671FYes, I'd imagine so.\x02",
    )

    CloseMessageWindow()

    def lambda_F81():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F81)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x10,
        (
            "#671FThe candelabrum is said to have \x01",
            "been made, at great pains, by the\x01",
            "townsfolk and given as a gift.\x02\x03",
            "#670FThat might explain the 'give\x01",
            "praise to the spirit' part.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#501FOhh, I get it.\x02\x03",
            "So, what about the last part?\x02\x03",
            "Sounds like it wants us to look\x01",
            "in a specific direction.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F'Look to the three-eyed giant\x01",
            "which towers over this\x01",
            "settlement...'\x02\x03",
            "Well, it certainly SOUNDS like\x01",
            "it's trying to tell us where to\x01",
            "go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002FAnd the destination has to\x01",
            "be important, somehow.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#042FThe 'settlement' bit probably\x01",
            "refers to Ruan...\x02\x03",
            "So there must be some kind of\x01",
            "'three-eyed giant' somewhere\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#505FHmm... A giant...\x02\x03",
            "Well, it's obviously a clue.\x01",
            "I'll make a note of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "#673FI can be of little use\x01",
            "in this matter.\x02\x03",
            "#670FI must be off soon, as I have\x01",
            "other work to which I must\x01",
            "attend.\x02\x03",
            "And so, I shall leave you\x01",
            "to your investigation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_132A():
        TurnDirection(0x101, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_132A)

    def lambda_1338():
        TurnDirection(0x105, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1338)
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#006FSure thing.\x02\x03",
            "So, first thing is to search\x01",
            "this room, top to bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#672FThat won't be necessary.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FWhy not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671FIt has already been looked\x01",
            "over by the residents.\x02\x03",
            "I'd like for you to search\x01",
            "the surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#671FThe card left you with a\x01",
            "distinct clue to follow.\x02\x03",
            "Don't tarry.\x02\x03",
            "That candelabrum must be recovered. \x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 400)

    ChrTalk(
        0x102,
        (
            "#015FI see...\x02\x03",
            "#010FThen we will abide by your wishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FI guess the client is always right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        (
            "#673FPlease understand, I have no\x01",
            "desire to interfere with the\x01",
            "professionals in this matter.\x02\x03",
            "I greatly appreciate your understanding.\x02\x03",
            "#670FNow, I'll leave you to concentrate.\x02\x03",
            "I'll be upstairs, so let me\x01",
            "know if you find anything out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164A():

        label("loc_164A")

        TurnDirection(0x101, 0x10, 0)
        OP_48()
        Jump("loc_164A")

    QueueWorkItem2(0x101, 1, lambda_164A)

    def lambda_165B():

        label("loc_165B")

        TurnDirection(0x102, 0x10, 0)
        OP_48()
        Jump("loc_165B")

    QueueWorkItem2(0x102, 1, lambda_165B)

    def lambda_166C():

        label("loc_166C")

        TurnDirection(0x105, 0x10, 0)
        OP_48()
        Jump("loc_166C")

    QueueWorkItem2(0x105, 1, lambda_166C)
    OP_8E(0x10, 0x2134, 0x0, 0x4B0, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    SetChrPos(0x10, 4530, 0, 36330, 90)
    Sleep(1000)

    def lambda_16B3():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B3)

    def lambda_16C1():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16C1)

    def lambda_16CF():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16CF)
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x11, 0x320)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#003FMan, this is a strange case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI guess we just have to see\x01",
            "where that card leads us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#040FThere must be a hint somewhere\x01",
            "in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FI guess we'll just have to be\x01",
            "patient and stay focused.\x02\x03",
            "Come on, let's get moving.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    OP_8C(0x10, 0, 0)
    OP_4B(0x10, 255)
    Return()

    # Function_0_66 end

    def Function_1_1838(): pass

    label("Function_1_1838")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_1853():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1853)
    OP_8E(0xFE, 0x1F4, 0xFFFFFE0C, 0xC8, 0x7D0, 0x0)
    Return()

    # Function_1_1838 end

    def Function_2_1874(): pass

    label("Function_2_1874")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_1894():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1894)
    OP_8E(0xFE, 0xFFFFFE0C, 0xFFFFFE0C, 0xFFFFFED4, 0x7D0, 0x0)
    Return()

    # Function_2_1874 end

    def Function_3_18B5(): pass

    label("Function_3_18B5")

    Sleep(400)
    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)

    def lambda_18DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18DA)
    OP_8E(0xFE, 0x12C, 0xFFFFFE0C, 0xFFFFFAEC, 0x7D0, 0x0)
    Return()

    # Function_3_18B5 end

    def Function_4_18FB(): pass

    label("Function_4_18FB")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    SetChrPos(0x101, 500, 0, 200, 0)
    SetChrPos(0x102, -500, 0, 200, 0)
    SetChrPos(0x105, 300, 0, -1300, 0)
    SetChrPos(0x8, 0, 0, 1800, 180)
    SetChrPos(0x10, 1000, 0, 2000, 180)
    OP_44(0x10, 0xFF)
    OP_44(0x8, 0xFF)
    OP_6D(200, 0, 300, 2000)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F...And that's the story.\x02\x03",
            "We got the candelabrum back,\x01",
            "undamaged...\x02\x03",
            "#015FBut we haven't found any\x01",
            "clues as to the whereabouts\x01",
            "of the thief.\x02\x03",
            "All we know is that he calls\x01",
            "himself 'Phantom Thief B.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F*sigh* If only we'd found out\x01",
            "about the fake sooner...\x02\x03",
            "He disappeared while we were\x01",
            "running around in circles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#661FNo, no... You've all done\x01",
            "a fine job.\x02\x03",
            "The main thing is that the\x01",
            "Sapphire Glim has been\x01",
            "recovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#678FThe mayor is right.\x02\x03",
            "You've done exactly what\x01",
            "was asked of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FThank you for your kind words...\x02\x03",
            "#013F...but the fact is, we still\x01",
            "allowed the thief to escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FYeah...\x02\x03",
            "We can't just let him get\x01",
            "away with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012FWe'd like your permission to\x01",
            "continue the investigation.\x02\x03",
            "If possible, we want to search\x01",
            "the estate for any further clues.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#662FNo, that's really not necessary.\x02\x03",
            "My request did not require you\x01",
            "to catch the culprit, after all.\x02\x03",
            "You brought back the candelabrum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012FBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#662FJoshua...\x02\x03",
            "I understand your passion for\x01",
            "upholding justice.\x02\x03",
            "But there are other, more\x01",
            "important crimes which must\x01",
            "be answered for.\x02\x03",
            "I do not wish to further monopolize\x01",
            "your time over something so trivial.\x02\x03",
            "#664FI've no doubt that there are others\x01",
            "out there who are waiting for a\x01",
            "bracer's help.\x02\x03",
            "It would please me if you helped\x01",
            "those in greater need first.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x8, 400)

    ChrTalk(
        0x10,
        "#672FMayor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F...\x02\x03",
            "...Understood.\x02\x03",
            "#010FThen, we will close our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#505FHmph... Oh, fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x8,
        (
            "#661FAnd of course, I will compensate\x01",
            "you fully for your time and\x01",
            "effort.\x02\x03",
            "#660FNow, if you'll excuse my\x01",
            "rudeness, I must leave.\x02\x03",
            "I wish you the best of luck\x01",
            "in your future endeavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FWe'll also be on our way, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2200   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_18FB end

    SaveToFile()

Try(main)

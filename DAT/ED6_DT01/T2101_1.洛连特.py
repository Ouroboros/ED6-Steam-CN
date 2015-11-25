from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2101.x',
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
        "Function_1_10CD",         # 01, 1
        "Function_2_29D5",         # 02, 2
        "Function_3_2A03",         # 03, 3
        "Function_4_2A33",         # 04, 4
        "Function_5_2A4F",         # 05, 5
        "Function_6_2A6B",         # 06, 6
        "Function_7_2A87",         # 07, 7
        "Function_8_3000",         # 08, 8
        "Function_9_36F0",         # 09, 9
        "Function_10_42E7",        # 0A, 10
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222")
    OP_28(0x21, 0x1, 0x2000)

    ChrTalk(
        0xFE,
        "Oh, it's you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry to say, but I found the key.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FOh, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "Turns out that I was right;\x01",
            "I did drop it near Aqua Rossa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I couldn't do as\x01",
            "you asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry to put you out like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000FIt's okay. I'm just glad you\x01",
            "found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a relief.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "Well, if I drop another key,\x01",
            "I'll let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509FHold on a second.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C9")

    label("loc_222")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_362")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293")

    ChrTalk(
        0x101,
        (
            "#000FGood afternoon, Harg.\x02\x03",
            "We have a question for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B")

    label("loc_293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")

    ChrTalk(
        0x102,
        (
            "#010FSorry to bother you while\x01",
            "you're working.\x02\x03",
            "We have something we wanted\x01",
            "to ask you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35B")

    label("loc_2FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")

    ChrTalk(
        0x105,
        (
            "#040FPardon us, Mr. Harg.\x02\x03",
            "We had a question for you,\x01",
            "if you don't mind...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35B")

    Call(1, 1)
    Jump("loc_10C9")

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7C")
    EventBegin(0x0)
    OP_28(0x21, 0x4, 0x4)
    OP_28(0x21, 0x4, 0x8)
    OP_28(0x21, 0x1, 0x1)
    OP_28(0x21, 0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp022_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 41040, -6550, 32140, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")

    ChrTalk(
        0x101,
        (
            "#000FExcuse us.\x02\x03",
            "Are you Harg?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49D")

    label("loc_414")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")

    ChrTalk(
        0x102,
        (
            "#010FPardon the interruption...\x02\x03",
            "Are you Harg, by any chance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49D")

    label("loc_466")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D")

    ChrTalk(
        0x105,
        "#040FPardon me, but are you Mr. Harg?\x02",
    )

    CloseMessageWindow()

    label("loc_49D")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        "Yeah, that's me...\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        "Oh! Are you guys bracers?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#006FYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FDid you happen to lose a\x01",
            "warehouse key?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "Yes, I did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was working with the barrels\x01",
            "around the crane the other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I musta dropped it\x01",
            "somewhere around there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_6DD")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505FHmm? Barrels around the crane?\x02\x03",
            "#002FHey, Joshua. Do you suppose...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010FYeah, sounds like it.\x02\x03",
            "I think it's the answer to the\x01",
            "riddle written on that card.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        "#010F...Sorry. Please, continue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O-Okay.\x02",
    )

    CloseMessageWindow()

    label("loc_6DD")


    ChrTalk(
        0xFE,
        (
            "I was waiting around to have\x01",
            "a drink at the Aqua Rossa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I probably dropped it in\x01",
            "that area.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801")

    ChrTalk(
        0xFE,
        "That's really all I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FWe'll go check it out.\x02\x03",
            "If you should happen to remember\x01",
            "anything else, please let us know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "See you later.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    TalkEnd(0xF)
    Jump("loc_B79")

    label("loc_801")


    ChrTalk(
        0xFE,
        (
            "Once I got to feeling good 'n\x01",
            "toasty, I decided to take a\x01",
            "walk around here...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xFE, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F?!\x02\x03",
            "You were wandering around\x01",
            "the harbor drunk?\x02\x03",
            "What if you dropped it in the water?\x01",
            "What if YOU fell in the water?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "Whaddya expect? I couldn't resist\x01",
            "the ocean air, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#007F*sigh* Well, talking isn't getting\x01",
            "us anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C3")

    ChrTalk(
        0x105,
        "#045F...So it would seem.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9EF")

    label("loc_9C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EF")

    ChrTalk(
        0x136,
        "#045F...So it would seem.\x02",
    )

    CloseMessageWindow()

    label("loc_9EF")


    ChrTalk(
        0xFE,
        (
            "Well, I figure I musta dropped\x01",
            "it somewhere in the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FI guess we've got some\x01",
            "walking around to do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010FIndeed.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "I'm sorry... I'm not tryin' to\x01",
            "make your lives any tougher.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0xFE,
        (
            "I've gotta get back to work.\x01",
            "Lemme know if you find it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FAnd please contact us if you\x01",
            "think of anything else.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "Yup, you bet.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    TalkEnd(0xF)

    label("loc_B79")

    Jump("loc_10C9")

    label("loc_B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C2")
    EventBegin(0x0)
    OP_4A(0xF, 255)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x1, 0x20)
    OP_3F(0x334, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")

    ChrTalk(
        0x101,
        (
            "#000FMr. Harg, do you have a second?\x02\x03",
            "About that key...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, well, um...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_C12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")

    ChrTalk(
        0x102,
        (
            "#010FSorry to bother you while\x01",
            "you're working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whatcha need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, well, um...\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE5")

    ChrTalk(
        0x105,
        (
            "#040FPardon us, Mr. Harg.\x01",
            "I hate to interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whatcha need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, well, um...\x02",
    )

    CloseMessageWindow()

    label("loc_CE5")

    Jump("loc_E6B")

    label("loc_CE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(
        0x101,
        "#508FHey there, Mr. Harg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whoa! Keep your voice down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The others are gonna find me out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008FOh. Oopsie.\x02\x03",
            "Anyway, about that key...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_DA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E07")

    ChrTalk(
        0x102,
        (
            "#010FSorry to bother you while\x01",
            "you're working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whatcha need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_E6B")

    label("loc_E07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6B")

    ChrTalk(
        0x105,
        (
            "#040FPardon us, Mr. Harg.\x01",
            "I hate to interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whatcha need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that...\x02",
    )

    CloseMessageWindow()

    label("loc_E6B")


    ChrTalk(
        0x101,
        (
            "#006FWe found something.\x02\x03",
            "This is the key, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "Warehouse Key\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "This is it, yep! No bones about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, thanks, you guys.\x01",
            "You really saved my skin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Say...why's it all tangled up\x01",
            "with fishing line?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506FHa ha ha...\x01",
            "It's kind of a long story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmmm...well, no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I gotta split. Thanks again.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Warehouse Key] \x07\x00",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(
        0x102,
        (
            "#014FPardon us...\x02\x03",
            "I need to ask you something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Call(1, 1)

    label("loc_10BD")

    EventEnd(0x1)
    Jump("loc_10C9")

    label("loc_10C2")

    TalkEnd(0xF)
    Call(0, 6)

    label("loc_10C9")

    TalkEnd(0xF)
    Return()

    # Function_0_66 end

    def Function_1_10CD(): pass

    label("Function_1_10CD")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        "Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What do you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FI was wondering what kind of\x01",
            "work you were doing when\x01",
            "you lost the key.\x02\x03",
            "You said you were moving\x01",
            "the barrels near the crane\x01",
            "to the warehouse...\x02\x03",
            "...Is that correct?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "Yep, sounds right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was actually just one barrel, though.\x01",
            "It was in the way of the crane, see, so\x01",
            "it had to be put in storage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I lost the key sometime\x01",
            "after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FSorry to be a bother, but is\x01",
            "there any way we could get\x01",
            "into the warehouse?\x02\x03",
            "We'd like to examine that barrel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm... Well, management doesn't\x01",
            "approve of outsiders entering our\x01",
            "warehouses. It's prohibited, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The stuff that's stored there is\x01",
            "supposed to be secure, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My job's at stake, so I really\x01",
            "can't let you inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505FMan...that's a problem, then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "Still, I owe you one.\x01",
            "I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You just want to check out\x01",
            "that one barrel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010FYes, that's correct.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "Well, I can take it out\x01",
            "for a spell, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That way, you can look it over\x01",
            "all you want, without ever having\x01",
            "to go inside. Hooray for loopholes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508FAh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FThanks.\x01",
            "That would be a huge help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Follow me, then.\x02",
    )

    CloseMessageWindow()
    Fade(2000)
    OP_6C(135000, 0)

    def lambda_15A6():
        OP_6D(23520, 1000, 4150, 4000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15A6)
    SetChrPos(0xFE, 23520, 1000, 4150, 180)
    OP_51(0x10, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x5BE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1036), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x102, 180, 0)
    OP_51(0x101, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x101, 180, 0)
    OP_51(0x105, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x105, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x105, 180, 0)
    OP_0D()
    Sleep(2000)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x3C)
    OP_73(0x15)
    OP_6F(0x15, 60)
    Sleep(1000)

    def lambda_16A9():
        OP_6D(22780, 0, 5890, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_16A9)
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    OP_90(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
    WaitChrThread(0x18, 0x1)

    ChrTalk(
        0xFE,
        "#4POkay, it's open.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#4PHang on a second here.\x02",
    )

    CloseMessageWindow()

    def lambda_171E():
        OP_6D(23920, 500, 4380, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_171E)
    ClearChrFlags(0x18, 0x80)
    OP_8E(0x18, 0x5BF4, 0x3E8, 0xFA0, 0x3E8, 0x0)
    ClearChrFlags(0x18, 0x4)
    OP_4A(0x18, 255)
    WaitChrThread(0x10, 0x1)
    OP_8C(0xFE, 180, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0xFE,
        "#1POh, Mr. Portos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1PWhatcha doing around here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4POh, I just had a hunch about\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PSo I used the duplicate key to\x01",
            "get in the warehouse, and check\x01",
            "on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1PHuh? A duplicate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1PDidn't even know there\x01",
            "was one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#4PAnyway, who are these folks?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "#1POh, they're bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1PThey want to look over that barrel\x01",
            "I moved in here earlier.\x01",
            "S'part of their investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#4PAh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PBut I'm afraid that only authorized\x01",
            "personnel are allowed inside the\x01",
            "warehouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 400)

    ChrTalk(
        0xFE,
        (
            "#1PYeah, but I'm the one who\x01",
            "moved it in there in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#1PShould be okay if I bring it\x01",
            "outside for a short while so\x01",
            "they can look it over, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PYes, that should be fine. Please,\x01",
            "assist them in their investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PSurprised to see bracers coming\x01",
            "all this way for an investigation,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PSuch young ones, too! You guys\x01",
            "do some admirable work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1P#001FHeh heh heh...\x01",
            "Well, we do all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#4PIf you need any information,\x01",
            "feel free to ask Harg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#4PNow, if you'll excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1PThank you, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_1BC7():

        label("loc_1BC7")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_1BC7")

    QueueWorkItem2(0xFE, 1, lambda_1BC7)

    def lambda_1BD8():

        label("loc_1BD8")

        TurnDirection(0x101, 0x18, 0)
        OP_48()
        Jump("loc_1BD8")

    QueueWorkItem2(0x101, 1, lambda_1BD8)

    def lambda_1BE9():

        label("loc_1BE9")

        TurnDirection(0x102, 0x18, 0)
        OP_48()
        Jump("loc_1BE9")

    QueueWorkItem2(0x102, 1, lambda_1BE9)

    def lambda_1BFA():

        label("loc_1BFA")

        TurnDirection(0x105, 0x18, 0)
        OP_48()
        Jump("loc_1BFA")

    QueueWorkItem2(0x105, 1, lambda_1BFA)
    SetChrFlags(0x18, 0x40)
    OP_8E(0x18, 0x6E0A, 0x0, 0x215C, 0x7D0, 0x0)
    OP_8E(0x18, 0x73B4, 0x3E8, 0x3840, 0x7D0, 0x0)
    SetChrFlags(0x18, 0x80)
    OP_44(0xFE, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)

    def lambda_1C4D():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C4D)

    def lambda_1C5B():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C5B)

    def lambda_1C69():
        OP_8C(0x2, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1C69)
    OP_8C(0xFE, 0, 400)
    Sleep(400)

    def lambda_1C83():
        OP_8C(0x0, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C83)

    def lambda_1C91():
        OP_8C(0x1, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C91)
    OP_8C(0x2, 180, 400)

    ChrTalk(
        0xFE,
        (
            "#2PAll righty...\x01",
            "I'll bring the barrel.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(23740, 0, 5560, 0)
    OP_72(0x1D, 0x4)
    OP_71(0x1D, 0x2)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, 23550, 500, 4740, 180)
    OP_8C(0x101, 180, 0)
    OP_8C(0x102, 180, 0)
    OP_8C(0x105, 180, 0)
    OP_8C(0xFE, 180, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(800)
    OP_94(0x1, 0xFE, 0xB4, 0x12C, 0x3E8, 0x0)
    OP_4A(0xFE, 255)
    ClearChrFlags(0xFE, 0x40)
    Sleep(400)
    OP_8C(0xFE, 0, 400)

    ChrTalk(
        0xFE,
        "#2PPhew! Sorry for the long wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2PHere's the barrel you wanted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004FWow... This thing is huge!\x02",
    )

    CloseMessageWindow()

    def lambda_1DD5():
        OP_6D(24500, 1000, 3980, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DD5)
    OP_43(0x102, 0x1, 0x1, 0x2)
    OP_43(0x105, 0x1, 0x1, 0x3)
    OP_43(0xFE, 0x1, 0x1, 0x4)
    OP_8E(0x101, 0x5FDC, 0x1F4, 0x1266, 0x3E8, 0x0)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        (
            "#000F#1PAnd you actually carried it\x01",
            "all by yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "#1PHa ha...\x01",
            "Never underestimate a dockhand!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_63(0x102)
    Sleep(800)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        "#014F#2PI found the card, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1F1A():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F1A)

    def lambda_1F28():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F28)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#004F#1PWhoa, really?!\x02",
    )

    CloseMessageWindow()

    def lambda_1F59():
        OP_6D(23220, 500, 4740, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F59)
    OP_43(0x101, 0x1, 0x1, 0x6)
    OP_8C(0x102, 45, 400)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'I must apologize most profoundly. For the barrel\x01",
            "to have been moved was an error most inopportune.\x01",
            "But the Warehouse Key was recovered, and you have\x01",
            "made it here. I will reveal the truth unto you.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Your reward will be what you have sought. Look\x01",
            "within the barrel. The candelabrum you find will,\x01",
            "no doubt, be returned to its rightful owner. Ah,\x01",
            "time grows short. We will meet again.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#003F#3PI've got a bad feeling about this...\x02\x03",
            "This weirdo must have been\x01",
            "close by, watching us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043FIndeed...\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#014F#4PHey, look at the card...\x02\x03",
            "Some of the ink is still wet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x105,
        "#044F#4P#1K...?!\x02",
    )


    ChrTalk(
        0x101,
        "#004F#3P#1KWhat?!\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()
    SetChrPos(0x18, 31010, 0, 9300, 119)
    ClearChrFlags(0x18, 0x80)

    def lambda_22D7():
        OP_6D(25540, 0, 5950, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_22D7)
    OP_8E(0x18, 0x7170, 0x0, 0x196E, 0x7D0, 0x0)
    OP_8C(0x18, 270, 0)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x18, 0x672A, 0x0, 0x1932, 0xBB8, 0x0)
    Sleep(400)

    ChrTalk(
        0x18,
        (
            "Hey, what do you think you're\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2385():
        TurnDirection(0x0, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2385)

    def lambda_2393():
        TurnDirection(0x1, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2393)

    def lambda_23A1():
        TurnDirection(0x2, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_23A1)
    TurnDirection(0xFE, 0x18, 400)

    ChrTalk(
        0xFE,
        "Huh?! Oh, uh...Mr. Portos.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You said earlier that this\x01",
            "would be okay.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x18,
        "???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "What are you talking about?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        "#012F#4PDamn. We've been had.\x02",
    )

    CloseMessageWindow()

    def lambda_248A():
        OP_6D(24290, 500, 4740, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_248A)

    def lambda_24A2():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_24A2)

    def lambda_24B0():
        TurnDirection(0x18, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_24B0)

    def lambda_24BE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24BE)
    TurnDirection(0x101, 0x102, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x101,
        (
            "#004F#3PWhoa, no way!\x02\x03",
            "You were just here a little\x01",
            "while ago, and...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4PIt must have been someone\x01",
            "posing as him.\x02\x03",
            "The criminal may have worn a\x01",
            "disguise and used the opportunity\x01",
            "to plant the card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F#5POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F#3PWell, then we need to get\x01",
            "after him!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25FB():

        label("loc_25FB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_25FB")

    QueueWorkItem2(0xFE, 1, lambda_25FB)

    def lambda_260C():

        label("loc_260C")

        TurnDirection(0x18, 0x101, 0)
        OP_48()
        Jump("loc_260C")

    QueueWorkItem2(0x18, 1, lambda_260C)

    def lambda_261D():

        label("loc_261D")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_261D")

    QueueWorkItem2(0x105, 1, lambda_261D)

    def lambda_262E():

        label("loc_262E")

        TurnDirection(0x102, 0x101, 0)
        OP_48()
        Jump("loc_262E")

    QueueWorkItem2(0x102, 1, lambda_262E)

    def lambda_263F():
        OP_8E(0x101, 0x745E, 0x208, 0x32F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_263F)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    ChrTalk(
        0x105,
        "#044F#2POh...! Estelle!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0xFE, 0x1)
    OP_44(0x18, 0x1)

    ChrTalk(
        0x102,
        "#014F#4POff she goes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        (
            "#042F#5PJoshua, shouldn't we do\x01",
            "something?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#013F#4PI'm afraid it's probably too late.\x02\x03",
            "We messed up when we didn't\x01",
            "notice the impostor before.\x02\x03",
            "#015FI doubt Estelle will find any\x01",
            "trace of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#043F#5PAh... I see...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4PLet's just make sure the\x01",
            "candelabrum isn't damaged.\x02\x03",
            "Retrieving it was our main\x01",
            "priority, not catching the perp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#042F#5PYou're right.\x02\x03",
            "It was written that it'd be in\x01",
            "this barrel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#4PI pray that's true.\x02",
    )

    CloseMessageWindow()

    def lambda_28A4():
        OP_8E(0x18, 0x6144, 0x0, 0x1AF4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_28A4)

    def lambda_28BF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28BF)
    Sleep(400)

    def lambda_28D2():
        OP_8C(0x102, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_28D2)
    OP_8E(0x105, 0x5B9A, 0x1F4, 0x12A2, 0x3E8, 0x0)
    OP_8C(0x105, 180, 400)
    Sleep(800)
    OP_62(0x18, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x18, 0x1)
    Sleep(800)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F#4POh, man...\x02\x03",
            "I hope she isn't too disappointed\x01",
            "that we're opening this without\x01",
            "her...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0xFE, 4620, -1800, 22750, 270)
    OP_4B(0xF, 255)
    SetChrFlags(0x18, 0x80)
    OP_71(0x1D, 0x4)
    OP_28(0x20, 0x1, 0x200)
    NewScene("ED6_DT01/T2210   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0xF)
    Return()

    # Function_1_10CD end

    def Function_2_29D5(): pass

    label("Function_2_29D5")

    OP_8E(0x102, 0x57E4, 0x3E8, 0xF96, 0x3E8, 0x0)
    OP_8C(0x102, 90, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Return()

    # Function_2_29D5 end

    def Function_3_2A03(): pass

    label("Function_3_2A03")

    OP_8E(0x105, 0x582A, 0x0, 0x14D2, 0x3E8, 0x0)
    OP_8E(0x105, 0x587A, 0xFA, 0x1342, 0x3E8, 0x0)
    OP_8C(0x105, 135, 400)
    Return()

    # Function_3_2A03 end

    def Function_4_2A33(): pass

    label("Function_4_2A33")

    OP_8E(0xFE, 0x5C08, 0x0, 0x19FA, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_2A33 end

    def Function_5_2A4F(): pass

    label("Function_5_2A4F")

    OP_8E(0x102, 0x588E, 0x2EE, 0x11BC, 0x7D0, 0x0)
    OP_8C(0x102, 90, 400)
    Return()

    # Function_5_2A4F end

    def Function_6_2A6B(): pass

    label("Function_6_2A6B")

    OP_8E(0x101, 0x5D3E, 0x1F4, 0x1266, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Return()

    # Function_6_2A6B end

    def Function_7_2A87(): pass

    label("Function_7_2A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B76")
    OP_8B(0x0, 0xA06E, 0x86A6, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(
        0x101,
        (
            "#002F(I don't like it, but we need to\x01",
            "get to the warehouse, and fast! )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_2AFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B70")

    ChrTalk(
        0x102,
        (
            "#012F(We really don't have time to\x01",
            "worry about anything else.)\x02\x03",
            "(Let's get inside that warehouse.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B70")

    TalkEnd(0xFF)
    Jump("loc_2FFF")

    label("loc_2B76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2C33")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_2B90")
    Call(1, 8)
    Jump("loc_2C30")

    label("loc_2B90")


    ChrTalk(
        0x101,
        (
            "#003FHmm... Looks like someone\x01",
            "dropped something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013FCheck it out. It might be useful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FMaybe we should pick up\x01",
            "some kind of tool or...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2C30")

    Jump("loc_2FFF")

    label("loc_2C33")

    EventBegin(0x0)
    OP_28(0x21, 0x1, 0x4)
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8B(0x0, 0xA050, 0x420351EC, 0x190)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C9F")

    ChrTalk(
        0x101,
        (
            "#004F...Hm?\x02\x03",
            "There's something shining\x01",
            "below us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D13")

    label("loc_2C9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE0")

    ChrTalk(
        0x102,
        (
            "#014F...?\x02\x03",
            "Looks like something's shining...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D13")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D13")

    ChrTalk(
        0x105,
        (
            "#044FOh...\x02\x03",
            "Something sparkled...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D13")

    Fade(1000)
    SetChrPos(0x101, 41040, -1650, 31310, 0)
    SetChrPos(0x102, 42040, -1650, 31230, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D5B")
    SetChrPos(0x105, 40040, -1650, 31130, 0)
    Jump("loc_2D79")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D79")
    SetChrPos(0x136, 40040, -1650, 31130, 0)

    label("loc_2D79")

    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004FIt's something in the water.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013FI wonder what it could be.\x02\x03",
            "If Mr. Harg were here, maybe\x01",
            "we could check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2ED1")

    ChrTalk(
        0x105,
        (
            "#043FBut what do we do?\x02\x03",
            "We can't exactly dive in\x01",
            "to have a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FMaybe...\x02\x03",
            "If we had something hooked\x01",
            "to snag it, then maybe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F71")

    ChrTalk(
        0x136,
        (
            "#043FBut what do we do?\x02\x03",
            "We can't exactly dive in\x01",
            "to have a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FMaybe...\x02\x03",
            "If we had something hooked\x01",
            "to snag it, then maybe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FEE")

    label("loc_2F71")


    ChrTalk(
        0x101,
        (
            "#505FBut what do we do?\x02\x03",
            "We can't exactly dive in\x01",
            "to have a look.\x02\x03",
            "If we had something hooked\x01",
            "to snag it, then maybe...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_2FFD")
    Call(1, 8)
    Jump("loc_2FFF")

    label("loc_2FFD")

    EventEnd(0x0)

    label("loc_2FFF")

    Return()

    # Function_7_2A87 end

    def Function_8_3000(): pass

    label("Function_8_3000")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 41040, -1650, 31430, 0)
    SetChrPos(0x102, 42040, -1650, 31230, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_304A")
    SetChrPos(0x105, 40040, -1650, 31130, 0)
    Jump("loc_3068")

    label("loc_304A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3068")
    SetChrPos(0x136, 40040, -1650, 31130, 0)

    label("loc_3068")

    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#003FHmm... Looks like someone\x01",
            "dropped something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013FCheck it out. It might be useful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505FMaybe we should pick up\x01",
            "some kind of tool or...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004FOh, I know!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Fade(1000)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(25000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 41040, -2000, 31900, 0)
    SetChrChipByIndex(0x101, 15)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x101,
        "#001FTa-dahhhh!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014FI get it. You're going to try\x01",
            "fishing it out?\x02\x03",
            "Isn't that going to be difficult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502FHeh heh... Just you sit back and\x01",
            "watch the magnificent Estelle\x01",
            "at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017FFine, fine...do as you please.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32F6")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        "#040FYou can do it, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508FYou betcha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3342")

    label("loc_32F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3342")
    TurnDirection(0x136, 0x101, 400)

    ChrTalk(
        0x136,
        "#040FYou can do it, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508FYou betcha!\x02",
    )

    CloseMessageWindow()

    label("loc_3342")

    Sleep(100)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_22(0x84, 0x0, 0x64)
    OP_99(0x101, 0x0, 0x6, 0x5DC)
    Sleep(400)
    OP_22(0x19, 0x0, 0x64)
    Sleep(1200)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x101)
    Sleep(700)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_99(0x101, 0x6, 0x3, 0x5DC)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    OP_22(0x18, 0x0, 0x64)
    OP_99(0x101, 0x3, 0x1, 0x5DC)
    Sleep(1000)
    OP_99(0x101, 0x10, 0x12, 0x5DC)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Snagged \x07\x02",
            "Warehouse Key\x07\x00",
            "!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xA050, 0xFFFFF98E, 0x7AC6, 0x258, 0xBB8)
    ClearChrFlags(0x101, 0x4)
    Sleep(400)

    def lambda_3469():
        OP_94(0x1, 0x101, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3469)
    Fade(1000)
    OP_6D(41040, -1650, 31830, 0)
    OP_6C(135000, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#508FCheck me out! I got it!\x02",
    )

    CloseMessageWindow()
    OP_3E(0x334, 1)
    OP_28(0x21, 0x1, 0x10)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014FPretty impressive.\x02\x03",
            "I have to admit, I didn't think\x01",
            "you'd be able to do it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F...Hey. That's not really the\x01",
            "same as congratulating me.\x02\x03",
            "#000FBut check it out! This looks\x01",
            "like the Warehouse Key that\x01",
            "Mr. Harg was talking about.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(
        0x102,
        (
            "#010FNo telling how it got dropped\x01",
            "in here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_365B")

    ChrTalk(
        0x105,
        (
            "#040FHa ha... Well, I'm sure he'll\x01",
            "feel better having it back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AC")

    label("loc_365B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_36AC")

    ChrTalk(
        0x136,
        (
            "#040FHa ha... Well, I'm sure he'll\x01",
            "feel better having it back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AC")


    ChrTalk(
        0x101,
        "#000FLet's bring it back to him.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010FOkay.\x02",
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_8_3000 end

    def Function_9_36F0(): pass

    label("Function_9_36F0")

    OP_28(0x20, 0x1, 0x8000)
    OP_28(0x20, 0x1, 0x20)
    OP_64(0x1, 0x1)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 20100, 0, 28900, 270)
    SetChrPos(0x102, 21200, 0, 29300, 270)
    SetChrPos(0x105, 22300, 0, 27900, 270)
    OP_6C(315000, 0)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002FHmmm...\x02\x03",
            "That's weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F#4PThis must be the 'Steel Crane,'\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#043F#2PThere are no barrels to\x01",
            "be found...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009FWell, what the heck is this\x01",
            "stupid clue supposed to mean,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x15, 400)

    ChrTalk(
        0x101,
        "#501F#6PHey, mister!\x02",
    )

    CloseMessageWindow()

    def lambda_3898():
        TurnDirection(0x102, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3898)

    def lambda_38A6():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_38A6)
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x15, 0x101, 400)
    OP_4A(0x15, 255)

    ChrTalk(
        0x15,
        "Hmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501FYou seen any barrels around here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Barrels?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Can't say that I can recall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The warehouse is packed full\x01",
            "of 'em, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_8C(0x15, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CE2")
    OP_28(0x20, 0x1, 0x100)

    ChrTalk(
        0x101,
        (
            "#505FAh...oh, well.\x02\x03",
            "...Hm? The warehouse?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x105, 0x101, 400)

    def lambda_3A81():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A81)

    ChrTalk(
        0x105,
        "#044FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505FUm... I was just thinking.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002FDidn't we find the Warehouse\x01",
            "Key earlier...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F#4PYes...at Mr. Harg's request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FAnd we haven't talked to him,\x01",
            "either, right?\x02\x03",
            "The barrels near the crane were\x01",
            "moved to the warehouse...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#014F#4PI get you.\x02\x03",
            "You're thinking that the barrels\x01",
            "that were here are all inside now.\x02\x03",
            "#010FYou're probably right. \x01",
            "Nice going, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001FHeh heh heh... It DOES happen\x01",
            "from time to time.\x02\x03",
            "Okay, let's go see what Mr. Harg\x01",
            "has to say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E4")

    label("loc_3CE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_406A")
    OP_28(0x20, 0x1, 0x80)

    ChrTalk(
        0x101,
        (
            "#505FAh...oh, well.\x02\x03",
            "...Hm? The warehouse?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x105, 0x101, 400)

    def lambda_3DA3():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DA3)

    ChrTalk(
        0x105,
        "#044FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505FUm... I was just thinking.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#002FDo you remember what he\x01",
            "said before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PYou mean Mr. Harg's request?\x02\x03",
            "He said he lost the Warehouse Key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002FRight. And we haven't talked\x01",
            "to him since then, either, right?\x02\x03",
            "The barrels near the crane were\x01",
            "moved to the warehouse...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#014F#4PI get you.\x02\x03",
            "You're thinking that the barrels\x01",
            "that were here are all inside now.\x02\x03",
            "#010FYou're probably right. \x01",
            "Nice going, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#001FHeh heh heh... It DOES happen\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4POkay, let's go talk with Mr. Harg.\x02\x03",
            "Maybe then, we can make\x01",
            "some real progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_42E4")

    label("loc_406A")

    OP_28(0x20, 0x1, 0x40)

    ChrTalk(
        0x101,
        (
            "#505FAh...oh, well.\x02\x03",
            "It still bugs me, though.\x01",
            "The trail's just petered out.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x10, 0x7D0)

    def lambda_410E():
        TurnDirection(0x105, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_410E)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F#4PThere should be some information\x01",
            "about the barrel...\x02\x03",
            "But right now, it looks like\x01",
            "there's nothing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#003FThere's got to be something in\x01",
            "here, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PShould we go and look into\x01",
            "another request?\x02\x03",
            "If there's more information to\x01",
            "be had in here, I don't know\x01",
            "where it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006FYeah, I guess we should.\x02\x03",
            "I'm not giving up on this one,\x01",
            "though. Let's keep an eye out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#4PAbsolutely.\x02\x03",
            "Let's get going, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E4")

    EventEnd(0x0)
    Return()

    # Function_9_36F0 end

    def Function_10_42E7(): pass

    label("Function_10_42E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_END)), "loc_4950")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E3")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4498")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_439F")

    ChrTalk(
        0x102,
        (
            "#014FHey, Estelle.\x02\x03",
            "We still haven't delivered the\x01",
            "Warehouse Key to Mr. Harg.\x02\x03",
            "#010FAnd we have to return the\x01",
            "fishing rod, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F2")

    label("loc_439F")


    ChrTalk(
        0x102,
        (
            "#014FHey, Estelle.\x02\x03",
            "We still haven't delivered the\x01",
            "Warehouse Key to Mr. Harg.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F2")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008FOh, I completely forgot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FLet's do that before we leave.\x01",
            "He's probably over at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E0")

    label("loc_4498")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4634")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_453B")

    ChrTalk(
        0x102,
        (
            "#014FOh, by the way...\x02\x03",
            "We still haven't given the\x01",
            "Warehouse Key to Mr. Harg.\x02\x03",
            "#010FAnd we have to return the\x01",
            "fishing rod, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458E")

    label("loc_453B")


    ChrTalk(
        0x102,
        (
            "#014FOh, by the way...\x02\x03",
            "We still haven't given the\x01",
            "Warehouse Key to Mr. Harg.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458E")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008FOh, I completely forgot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010FLet's do that before we leave.\x01",
            "He's probably over at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FOkay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E0")

    label("loc_4634")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E0")
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_46D7")

    ChrTalk(
        0x102,
        (
            "#014FOh, by the way...\x02\x03",
            "We still haven't given the\x01",
            "Warehouse Key to Mr. Harg.\x02\x03",
            "#010FAnd we have to return the\x01",
            "fishing rod, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472A")

    label("loc_46D7")


    ChrTalk(
        0x102,
        (
            "#014FOh, by the way...\x02\x03",
            "We still haven't given the\x01",
            "Warehouse Key to Mr. Harg.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472A")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        "#008FOh, I completely forgot...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044FWe ought to go and see\x01",
            "him, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010FAgreed. He's probably over\x01",
            "at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E0")

    Jump("loc_4932")

    label("loc_47E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4860")
    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010FBefore we go, let's give that\x01",
            "Warehouse Key to Mr. Harg.\x02\x03",
            "Odds are, he's over at the harbor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4932")

    label("loc_4860")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B8")

    ChrTalk(
        0x102,
        (
            "#010FBefore we go, we ought to give\x01",
            "that Warehouse Key to Mr. Harg.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4932")

    label("loc_48B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4932")
    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010FBefore we go, let's give that\x01",
            "Warehouse Key to Mr. Harg.\x02\x03",
            "Odds are, he's over at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4932")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4AC3")

    label("loc_4950")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_4AC3")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A45")
    OP_A2(0x0)

    ChrTalk(
        0x102,
        (
            "#010FWe also still have that fishing\x01",
            "rod we borrowed from the bar.\x02\x03",
            "We can't leave without returning it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505FUmm... We borrowed it from\x01",
            "the bar in the harbor, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#040FOh, the Aqua Rossa?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AA8")

    label("loc_4A45")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010FWe still have that fishing rod\x01",
            "we borrowed from the bar.\x02\x03",
            "Let's go bring it back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA8")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4AC3")

    Return()

    # Function_10_42E7 end

    SaveToFile()

Try(main)

from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2102.x',
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x20, 0x1, 0x10)
    Fade(1000)
    SetChrPos(0x102, 113500, 0, 102600, 90)
    SetChrPos(0x101, 112500, 0, 102300, 90)
    SetChrPos(0x105, 111200, 0, 103100, 90)
    OP_51(0xE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(135000, 0)

    def lambda_F9():
        OP_6C(155000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F9)

    def lambda_109():
        OP_69(0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_109)
    OP_6B(2800, 3000)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xE, 0x2)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#011F#3PI get it...the 'One-Eyed Lion.'\x02\x03",
            "I wonder if there's a way to keep\x01",
            "it from seeing you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#6PThis must be the 'Land Harbor.'\x02\x03",
            "No doubt about it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F#3PAll right, let's see what we\x01",
            "can find.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C32C), scpexpr(EXPR_PUSH_LONG, 0x1BB5C), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x19000), scpexpr(EXPR_PUSH_LONG, 0x190C8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_24A():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_24A)

    def lambda_25A():
        OP_69(0xE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_25A)
    SetChrFlags(0x102, 0x40)
    OP_8C(0x102, 0, 400)

    def lambda_274():
        OP_8E(0x101, 0x1BB5C, 0x0, 0x190C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_274)

    def lambda_28F():
        OP_8E(0x105, 0x1B7D8, 0x0, 0x19320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28F)
    OP_8E(0x102, 0x1BB5C, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1C1A6, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1C32C, 0x0, 0x19000, 0x7D0, 0x0)
    OP_8C(0x102, 225, 400)
    ClearChrFlags(0x102, 0x40)
    Sleep(600)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F#3POkay, I found the card.\x02\x03",
            "We should confirm its contents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006FRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Ah, seeker. The eyes of Aidios see only the\x01",
            "truth, and pass it on to you.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "'Beyond the drawbridge, look to the barrels\x01",
            "near the Steel Crane. Do so, and the blue\x01",
            "light will be revealed.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#509F#4PHmm...another weirdo clue. Now it's a\x01",
            "'Steel Crane'? Sounds suspiciously easy\x01",
            "to figure out this time...\x02\x03",
            "#505FThe drawbridge it mentions is\x01",
            "probably the one over in the\x01",
            "harbor.\x02\x03",
            "Ugh. How much longer are\x01",
            "we going to have to do this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#041F#4PHa ha. I'm sure we must be\x01",
            "nearing the end.\x02\x03",
            "We just have to keep going.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F#3POkay, Estelle. What do you\x01",
            "need to pick up your spirits?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#008F#4PUm...\x02\x03",
            "I-I'm just tired, is all.\x01",
            "I'm fine. Really!\x02\x03",
            "See? I'm ready to get back\x01",
            "in the game!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F#3PI swear...\x02",
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)

    def lambda_6AB():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6AB)
    OP_8E(0x102, 0x1C1A6, 0x0, 0x196A4, 0x7D0, 0x0)
    OP_8E(0x102, 0x1BB5C, 0x0, 0x196A4, 0x7D0, 0x0)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)

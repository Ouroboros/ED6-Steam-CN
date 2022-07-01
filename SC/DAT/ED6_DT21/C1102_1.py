import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1102_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1102_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C1102_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x514
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x02)
    OP_28(0x007D, 0x01, 0x0008)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '打倒了所有的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    EventEnd(0x03)

    Return()

# id: 0x0001 offset: 0xF9
@scena.Code('Init')
def Init():
    EventBegin(0x02)
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x000A, 75710, -500, 187310, 180)
    SetChrPos(0x0008, 76850, -500, 177570, 0)
    SetChrPos(0x0009, 74990, -500, 176460, 0)
    OP_6D(75660, -350, 200280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_1D(0x51)

    @scena.Lambda('lambda_0197')
    def lambda_0197():
        OP_6D(75710, -500, 187310, 8500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0197)

    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)
    Sleep(1000)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#4210490339V#2P真是的……\n',
            '被彻底打败。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_01F2')
    def lambda_01F2():
        OP_6D(75710, -500, 185000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_01F2)

    Sleep(2500)

    @scena.Lambda('lambda_020F')
    def lambda_020F():
        OP_8E(0x0008, 76850, -500, 185430, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_020F)

    Sleep(500)

    @scena.Lambda('lambda_022F')
    def lambda_022F():
        OP_8E(0x0009, 74990, -500, 184530, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_022F)

    WaitForThreadExit(0x0008, 0x0000)
    OP_6D(75710, -500, 187310, 4500)
    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 315, 400)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#4210490340V想不到那些游击士\n',
            '居然会闯进来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210490341V虽然全力以赴，\n',
            '不过，最后还是被击败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480490342V嗯，真是的──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480490343V那帮家伙\n',
            '总是妨碍我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#4210490344V哟，你认识他们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0480490345V别问了──\n',
            '先不管这些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0480490346V赶快把残骸收拾掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210490347V是啊……\n',
            '尽快撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4210490348V以巡逻型人形兵器的测试来说，\n',
            '这次的成果也非常足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)
    CreateThread(0x0008, 0x01, 0x01, 0x0002)
    OP_8C(0x0009, 0, 400)

    @scena.Lambda('lambda_0426')
    def lambda_0426():
        OP_69(0x0009, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0426)

    @scena.Lambda('lambda_0434')
    def lambda_0434():
        OP_6B(2600, 3500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0434)

    Sleep(1000)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0480490349V哼，不过……\n',
            '想不到他们对付巡逻型也这么棘手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480490350V那帮家伙的小命──\n',
            '估计也不会太长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT21/R1502._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0002 offset: 0x4D4
@scena.Code('ReInit')
def ReInit():
    OP_8E(0x0008, 76700, -500, 187310, 1500, 0x00)
    OP_8C(0x0008, 270, 400)

    Return()

# id: 0x0003 offset: 0x4F0
@scena.Code('func_03_4F0')
def func_03_4F0():
    OP_8E(0x0009, 74990, -500, 186160, 2000, 0x00)
    OP_8C(0x0009, 45, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

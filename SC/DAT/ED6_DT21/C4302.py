import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4302.x'
    header.mapIndex       = 216
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '尤莉亚上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '升降机用',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7320,
            triggerZ            = 0,
            triggerY            = 38820,
            triggerRange        = 1000,
            actorX              = 7320,
            actorZ              = 1000,
            actorY              = 38820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x13E
@scena.Code('Init')
def Init():
    MapSetFlags(0x10000000)
    Event(0, func_02_1AD)

    Return()

# id: 0x0001 offset: 0x148
@scena.Code('func_01_148')
def func_01_148():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A0',
    )

    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Jump('loc_1AC')

    def _loc_1A0(): pass

    label('loc_1A0')

    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 250)

    def _loc_1AC(): pass

    label('loc_1AC')

    Return()

# id: 0x0002 offset: 0x1AD
@scena.Code('func_02_1AD')
def func_02_1AD():
    MapClearFlags(0x00000001)
    MapClearFlags(0x00000080)
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x010A, 0x0008)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrSetBattleFlags(0x0009, 0x0020)
    CameraMove(250, 34000, -61740, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(20000, 0)
    OP_6E(389, 0)
    TalkSetChrName('正文（肖像表示）')
    OP_A1(0x000A, 0x0000)
    ChrSetPos(0x000A, 0, 50000, -61960, 0)
    OP_72(0x0000, 0x0004)
    Yield()
    OP_89(0x0008, 800, 70000, -62000, 0)
    OP_89(0x0009, -800, 70000, -62000, 0)
    CreateThread(0x000A, 0x01, 0x00, func_03_814)
    OP_C8(0x0200, 0x0046, 'C_PLAC03._CH', 0x01, 0x05DC)
    PlaySE(235, 0x00, 0x64)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_02B2')
    def lambda_02B2():
        CameraMove(250, -4000, -61740, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_02B2)

    @scena.Lambda('lambda_02CA')
    def lambda_02CA():
        OP_67(0, 9500, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02CA)

    @scena.Lambda('lambda_02E2')
    def lambda_02E2():
        CameraSetDistance(3200, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02E2)

    @scena.Lambda('lambda_02F2')
    def lambda_02F2():
        OP_6E(262, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_02F2)

    @scena.Lambda('lambda_0302')
    def lambda_0302():
        OP_6C(45000, 11000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0302)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_0326')
    def lambda_0326():
        ChrWalkTo(0x0009, -800, -4000, -60390, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0326)

    @scena.Lambda('lambda_0341')
    def lambda_0341():
        CameraMove(300, -4000, -58390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0341)

    @scena.Lambda('lambda_0359')
    def lambda_0359():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0359)

    Sleep(500)

    @scena.Lambda('lambda_0376')
    def lambda_0376():
        ChrWalkTo(0x0008, 800, -4000, -60470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0376)

    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0008, 260, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180200001V#2P#1068F呼～话说回来\n',
            '还真是相当棘手呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200002V两条腿快要酸死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 500)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0100200003V#170F#6P呵呵，安心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200004V这里是『封印区域』的最下层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200005V#2P#1062F哇，真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200006V#1061F哈哈～我还在想，如果你要是说\n',
            '“刚走了一半”的话该怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200007V#176F#6P呵呵，您谦虚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200008V#170F神父你作为圣职者，\n',
            '看来却经过相当的锻炼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200009V否则可无法胜任\n',
            '你的工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200010V#2P#1068F真是服了你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200011V#1062F不过……也好。\n',
            '利贝尔王家似乎和我们\n',
            '从以前开始就渊源颇深。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200012V#1060F对了、上尉。\n',
            '关于市长的那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200013V#170F#6P啊啊，『封印宝杖』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200014V我们遵从盟约，以指定的方法\n',
            '正在严加保管中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100200015V随时都可以交给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180200016V#2P#1061F感激不尽，真是帮大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180200017V#1060F那么……\n',
            '能把那个东西给我看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100200018V#178F#6P啊──在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 500)
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_073F')
    def lambda_073F():
        ChrWalkTo(0x0009, -60, -4000, -58630, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_073F)

    Sleep(500)

    ChrSetDirection(0x0008, 0, 500)
    ChrSetFlags(0x0008, 0x0040)

    @scena.Lambda('lambda_076B')
    def lambda_076B():
        ChrWalkTo(0x0008, -60, -4000, -58630, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_076B)

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_078B')
    def lambda_078B():
        ChrWalkTo(0x0009, 70, -4000, -42210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_078B)

    @scena.Lambda('lambda_07A6')
    def lambda_07A6():
        CameraMove(100, -4000, -48210, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07A6)

    @scena.Lambda('lambda_07BE')
    def lambda_07BE():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07BE)

    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        ChrWalkTo(0x0008, 70, -4000, -42210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_07DB)

    Sleep(2000)

    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    NewScene('ED6_DT21/C4303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x814
@scena.Code('func_03_814')
def func_03_814():
    @scena.Lambda('lambda_081A')
    def lambda_081A():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_081A)

    Sleep(8500)

    @scena.Lambda('lambda_083A')
    def lambda_083A():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_083A)

    Sleep(500)

    @scena.Lambda('lambda_085A')
    def lambda_085A():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_085A)

    Sleep(500)

    @scena.Lambda('lambda_087A')
    def lambda_087A():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_087A)

    CreateThread(0x000A, 0x02, 0x00, func_04_941)
    Sleep(300)

    @scena.Lambda('lambda_08A1')
    def lambda_08A1():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_08A1)

    Sleep(200)

    @scena.Lambda('lambda_08C1')
    def lambda_08C1():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 900, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_08C1)

    Sleep(200)

    @scena.Lambda('lambda_08E1')
    def lambda_08E1():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_08E1)

    Sleep(100)

    @scena.Lambda('lambda_0901')
    def lambda_0901():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 700, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0901)

    Sleep(100)

    @scena.Lambda('lambda_0921')
    def lambda_0921():
        ChrMoveTo(0x00FE, 0, -5500, -61960, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0921)

    Sleep(100)

    WaitForThreadExit(0x000A, 0x0000)

    Return()

# id: 0x0004 offset: 0x941
@scena.Code('func_04_941')
def func_04_941():
    OP_24(0x00EB, 0x5A)
    Sleep(300)

    OP_24(0x00EB, 0x50)
    Sleep(300)

    OP_24(0x00EB, 0x46)
    Sleep(300)

    OP_24(0x00EB, 0x3C)
    Sleep(200)

    OP_24(0x00EB, 0x32)
    Sleep(200)

    OP_24(0x00EB, 0x28)
    Sleep(200)

    OP_24(0x00EB, 0x1E)
    Sleep(100)

    OP_24(0x00EB, 0x14)
    Sleep(100)

    OP_24(0x00EB, 0x0A)
    Sleep(100)

    OP_23(0x00EB)

    Return()

# id: 0x0005 offset: 0x996
@scena.Code('func_05_996')
def func_05_996():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9E7',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_B89')

    def _loc_9E7(): pass

    label('loc_9E7')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6E',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 300)
    OP_70(0x0007, 500)
    OP_73(0x0007)
    OP_6F(0x0007, 500)
    OP_70(0x0007, 700)
    OP_71(0x0007, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x06, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x05, 0x06, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_B6E(): pass

    label('loc_B6E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B88',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_B88(): pass

    label('loc_B88')

    Return()

    def _loc_B89(): pass

    label('loc_B89')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

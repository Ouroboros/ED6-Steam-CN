import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0700_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0700   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0700.x'
    header.mapIndex       = 1
    header.bgm            = 60
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
        ('ED6_DT29/CH12590._CH', 'ED6_DT29/CH12590P._CP'),
        ('ED6_DT29/CH12591._CH', 'ED6_DT29/CH12591P._CP'),
        ('ED6_DT29/CH12600._CH', 'ED6_DT29/CH12600P._CP'),
        ('ED6_DT29/CH12601._CH', 'ED6_DT29/CH12601P._CP'),
        ('ED6_DT29/CH12610._CH', 'ED6_DT29/CH12610P._CP'),
        ('ED6_DT29/CH12611._CH', 'ED6_DT29/CH12611P._CP'),
        ('ED6_DT29/CH12620._CH', 'ED6_DT29/CH12620P._CP'),
        ('ED6_DT29/CH12621._CH', 'ED6_DT29/CH12621P._CP'),
        ('ED6_DT29/CH12630._CH', 'ED6_DT29/CH12630P._CP'),
        ('ED6_DT29/CH12631._CH', 'ED6_DT29/CH12631P._CP'),
        ('ED6_DT29/CH12640._CH', 'ED6_DT29/CH12640P._CP'),
        ('ED6_DT29/CH12641._CH', 'ED6_DT29/CH12641P._CP'),
        ('ED6_DT29/CH12650._CH', 'ED6_DT29/CH12650P._CP'),
        ('ED6_DT29/CH12651._CH', 'ED6_DT29/CH12651P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -7290,
            z           = -7200,
            y           = -490,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FC0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 7690,
            z           = -7200,
            y           = 490,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FC1,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = -7650,
            triggerY            = -650,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = -7650,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x176
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 5, 0x1E05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_185',
    )

    Event(0, func_03_324)

    Jump('loc_1A3')

    def _loc_185(): pass

    label('loc_185')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_195'),
        (0x00000065, 'loc_19C'),
        (-1, 'loc_1A3'),
    )

    def _loc_195(): pass

    label('loc_195')

    Event(0, func_0A_C26)

    Jump('loc_1A3')

    def _loc_19C(): pass

    label('loc_19C')

    Event(0, func_10_1112)

    Jump('loc_1A3')

    def _loc_1A3(): pass

    label('loc_1A3')

    Return()

# id: 0x0001 offset: 0x1A4
@scena.Code('func_01_1A4')
def func_01_1A4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 0, 0x1F00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1BD')

    def _loc_1B6(): pass

    label('loc_1B6')

    OP_6F(0x0001, 60)

    def _loc_1BD(): pass

    label('loc_1BD')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')
    OP_1B(0x00, 0x00, 0x000B)
    OP_1B(0x01, 0x00, 0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 0, 0x1FC0)),
            Expr.Return,
        ),
        'loc_1FB',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_1FB(): pass

    label('loc_1FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 1, 0x1FC1)),
            Expr.Return,
        ),
        'loc_207',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_207(): pass

    label('loc_207')

    Return()

# id: 0x0002 offset: 0x208
@scena.Code('func_02_208')
def func_02_208():
    UnlockAchievement(0x02, 0x0014, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 0, 0x1F00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_27C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03E0, 0, 0x1F00))

    Jump('loc_2E2')

    def _loc_27C(): pass

    label('loc_27C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_2E2(): pass

    label('loc_2E2')

    Jump('loc_316')

    def _loc_2E5(): pass

    label('loc_2E5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_316(): pass

    label('loc_316')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x324
@scena.Code('func_03_324')
def func_03_324():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33B',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)

    def _loc_33B(): pass

    label('loc_33B')

    CameraMove(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 0, 1050, -83970, 0)
    ChrSetPos(0x0102, 0, 1050, -83970, 0)
    ChrSetPos(0x00F8, 0, 1050, -83970, 0)
    ChrSetPos(0x00F9, 0, 1050, -83970, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F8, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F9, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_04_964)
    Sleep(800)

    @scena.Lambda('lambda_0435')
    def lambda_0435():
        CameraMove(140, 600, -78810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0435)

    CreateThread(0x0102, 0x00, 0x00, func_05_9CF)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_06_A3A)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_07_AA5)
    Sleep(600)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340716V#1004F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0000)

    ChrTalk(
        0x0102,
        (
            '#0020340717V#1044F#2P这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_C8(0x0200, 0x0046, 'C_PLAC21._CH', 0x01, 0x03E8)
    ShowPlaceName('翡翠之塔')
    CameraMove(3520, 11180, 56940, 0)
    OP_67(0, 3370, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0535')
    def lambda_0535():
        CameraMove(-170, 600, -78050, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0535)

    @scena.Lambda('lambda_054D')
    def lambda_054D():
        OP_67(0, 7500, -10000, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_054D)

    @scena.Lambda('lambda_0565')
    def lambda_0565():
        CameraSetDistance(3000, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0565)

    @scena.Lambda('lambda_0575')
    def lambda_0575():
        OP_6C(315000, 15000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0575)

    @scena.Lambda('lambda_0585')
    def lambda_0585():
        OP_6E(262, 15000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0585)

    WaitForThreadExit(0x0102, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340718V#1020F#5P等、等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340719V我们，确实\n',
            '应该进入了塔中吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65A',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340720V#1065F#6P空间转移……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340721V#1063F看来是被传送到\n',
            '其它的地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F8')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340722V#065F#6P空、空间转移……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340723V可能是被传送到\n',
            '其它的地方了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F8')

    def _loc_6C2(): pass

    label('loc_6C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_72D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340724V#047F#6P空间转移……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340725V#042F说不定是被传送到\n',
            '其它的地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F8')

    def _loc_72D(): pass

    label('loc_72D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_794',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340726V#074F#6P空间转移……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340727V#072F好像被传送到\n',
            '其它的地方了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F8')

    def _loc_794(): pass

    label('loc_794')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340728V#026F#6P空间转移……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340729V#022F好像被传送到\n',
            '其它的地方了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F8(): pass

    label('loc_7F8')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrSetDirection(0x0101, 180, 600)

    ChrTalk(
        0x0101,
        (
            '#0010340730V#1019F#2P你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340731V#1020F那、那么要爬上塔顶\n',
            '就不可能了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020340732V#1035F冷静点，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340733V#1040F既然会有布卢布兰出现\n',
            '这就表明必然有路可走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010340734V#1007F#4P确、确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340735V#1002F……嗯！\n',
            '总之慎重前进吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x03C0, 5, 0x1E05))
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x964
@scena.Code('func_04_964')
def func_04_964():
    @scena.Lambda('lambda_096A')
    def lambda_096A():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_096A)

    @scena.Lambda('lambda_0984')
    def lambda_0984():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0984)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_09AF')
    def lambda_09AF():
        ChrMoveTo(0x00FE, 610, 600, -77870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_09AF)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0005 offset: 0x9CF
@scena.Code('func_05_9CF')
def func_05_9CF():
    @scena.Lambda('lambda_09D5')
    def lambda_09D5():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_09D5)

    @scena.Lambda('lambda_09EF')
    def lambda_09EF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_09EF)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0A1A')
    def lambda_0A1A():
        ChrMoveTo(0x00FE, -470, 600, -78090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A1A)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0006 offset: 0xA3A
@scena.Code('func_06_A3A')
def func_06_A3A():
    @scena.Lambda('lambda_0A40')
    def lambda_0A40():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A40)

    @scena.Lambda('lambda_0A5A')
    def lambda_0A5A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A5A)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        ChrMoveTo(0x00FE, 630, 750, -79310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0A85)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0007 offset: 0xAA5
@scena.Code('func_07_AA5')
def func_07_AA5():
    @scena.Lambda('lambda_0AAB')
    def lambda_0AAB():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0AAB)

    @scena.Lambda('lambda_0AC5')
    def lambda_0AC5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0AC5)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0001)
    PlaySE(153, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ChrClearFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0AF0')
    def lambda_0AF0():
        ChrMoveTo(0x00FE, -540, 750, -79320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0AF0)

    WaitForThreadExit(0x00FE, 0x0002)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0008 offset: 0xB10
@scena.Code('func_08_B10')
def func_08_B10():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_B8A'),
        (0x00000001, 'loc_B90'),
        (-1, 'loc_B96'),
    )

    def _loc_B8A(): pass

    label('loc_B8A')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_B96')

    def _loc_B90(): pass

    label('loc_B90')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_B96')

    def _loc_B96(): pass

    label('loc_B96')

    Return()

# id: 0x0009 offset: 0xB97
@scena.Code('func_09_B97')
def func_09_B97():
    FadeOut(0, 0, -1)
    CameraMove(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000A offset: 0xC26
@scena.Code('func_0A_C26')
def func_0A_C26():
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 0, 1050, -83970, 0)
    ChrSetPos(0x0102, 0, 1050, -83970, 0)
    ChrSetPos(0x00F8, 0, 1050, -83970, 0)
    ChrSetPos(0x00F9, 0, 1050, -83970, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F8, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x00F9, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x00F8, 0x0004)
    ChrSetFlags(0x00F9, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrClearFlags(0x0102, 0x0001)
    ChrClearFlags(0x00F8, 0x0001)
    ChrClearFlags(0x00F9, 0x0001)
    OP_C8(0x0200, 0x0046, 'C_PLAC21._CH', 0x01, 0x03E8)
    ShowPlaceName('翡翠之塔')
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, func_04_964)
    Sleep(800)

    @scena.Lambda('lambda_0D40')
    def lambda_0D40():
        CameraMove(140, 600, -78810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D40)

    CreateThread(0x0102, 0x00, 0x00, func_05_9CF)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, func_06_A3A)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, func_07_AA5)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    CameraMove(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 610, 600, -77870, 0)
    ChrSetPos(0x0001, 610, 600, -77870, 0)
    ChrSetPos(0x0002, 610, 600, -77870, 0)
    ChrSetPos(0x0003, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0xE0F
@scena.Code('func_0B_E0F')
def func_0B_E0F():
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    MapClearFlags(0x00000001)
    CameraMove(-600, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3600, 0)
    OP_6C(219000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 680, 700, -81310, 180)
    ChrSetPos(0x0102, -330, 700, -81100, 180)
    ChrSetPos(0x00F8, 910, 750, -79600, 180)
    ChrSetPos(0x00F9, -270, 750, -79450, 180)
    CreateThread(0x0101, 0x00, 0x00, func_0C_EFE)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, func_0D_F83)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, func_0E_1008)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0F_108D)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    NewScene('ED6_DT21/R0303._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0xEFE
@scena.Code('func_0C_EFE')
def func_0C_EFE():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0F43')
    def lambda_0F43():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F43)

    @scena.Lambda('lambda_0F5D')
    def lambda_0F5D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0F5D)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000D offset: 0xF83
@scena.Code('func_0D_F83')
def func_0D_F83():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -2000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0FC8')
    def lambda_0FC8():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0FC8)

    @scena.Lambda('lambda_0FE2')
    def lambda_0FE2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0FE2)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000E offset: 0x1008
@scena.Code('func_0E_1008')
def func_0E_1008():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_104D')
    def lambda_104D():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_104D)

    @scena.Lambda('lambda_1067')
    def lambda_1067():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1067)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x000F offset: 0x108D
@scena.Code('func_0F_108D')
def func_0F_108D():
    ChrMoveToRelativeAsync(0x00FE, 0, 0, -3000, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0001)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(153, 0x00, 0x64)
    ChrSetFlags(0x00FE, 0x0004)
    ChrMoveToRelativeAsync(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_10D2')
    def lambda_10D2():
        OP_9E(0x00FE, 0, 100, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_10D2)

    @scena.Lambda('lambda_10EC')
    def lambda_10EC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_10EC)

    WaitForThreadExit(0x00FE, 0x0001)
    ChrMoveToRelativeAsync(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0010 offset: 0x1112
@scena.Code('func_10_1112')
def func_10_1112():
    EventBegin(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, -50, 84460, 0)
    ChrSetPos(0x0101, 500, -50, 83960, 180)
    ChrSetPos(0x0102, -500, -50, 83960, 180)
    ChrSetPos(0x00F8, 500, -50, 84960, 180)
    ChrSetPos(0x00F9, -500, -50, 84960, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0013)
    Call(0, 0x0014)
    Fade(500)
    CameraMove(80, 260, 81830, 0)
    ChrSetPos(0x0000, 80, 260, 81830, 180)
    ChrSetPos(0x0001, 80, 260, 81830, 180)
    ChrSetPos(0x0002, 80, 260, 81830, 180)
    ChrSetPos(0x0003, 80, 260, 81830, 180)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x120D
@scena.Code('func_11_120D')
def func_11_120D():
    EventBegin(0x00)
    Fade(500)
    ChrSetPos(0x0101, -500, -50, 84960, 0)
    ChrSetPos(0x0102, 500, -50, 84960, 0)
    ChrSetPos(0x00F8, -500, -50, 83960, 0)
    ChrSetPos(0x00F9, 500, -50, 83960, 0)
    OP_0D()
    Call(0, 0x0013)
    Call(0, 0x0015)
    NewScene('ED6_DT21/C0701._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x126B
@scena.Code('func_12_126B')
def func_12_126B():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0013 offset: 0x134A
@scena.Code('func_13_134A')
def func_13_134A():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0014 offset: 0x1429
@scena.Code('func_14_1429')
def func_14_1429():
    @scena.Lambda('lambda_142F')
    def lambda_142F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_142F)

    @scena.Lambda('lambda_1441')
    def lambda_1441():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1441)

    @scena.Lambda('lambda_1453')
    def lambda_1453():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1453)

    @scena.Lambda('lambda_1465')
    def lambda_1465():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1465)

    Sleep(2500)

    Return()

# id: 0x0015 offset: 0x1477
@scena.Code('func_15_1477')
def func_15_1477():
    @scena.Lambda('lambda_147D')
    def lambda_147D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_147D)

    @scena.Lambda('lambda_148F')
    def lambda_148F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_148F)

    @scena.Lambda('lambda_14A1')
    def lambda_14A1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_14A1)

    @scena.Lambda('lambda_14B3')
    def lambda_14B3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_14B3)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

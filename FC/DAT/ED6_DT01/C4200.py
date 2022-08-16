import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4200.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
            word_32         = 45,
            word_34         = 45,
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 1040,
            z           = 0,
            y           = 33740,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -13230,
            z           = 0,
            y           = 63010,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24830,
            z           = 0,
            y           = 62910,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -71240,
            z           = 0,
            y           = 42750,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -75480,
            z           = 0,
            y           = -690,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -32930,
            z           = 0,
            y           = -57110,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 20530,
            z           = 0,
            y           = -113240,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 280,
            z           = 0,
            y           = -131490,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 14700,
            z           = 0,
            y           = -124590,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x226
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x226
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -74020,
            triggerZ            = 0,
            triggerY            = -15990,
            triggerRange        = 1000,
            actorX              = -74020,
            actorZ              = 1500,
            actorY              = -16720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12830,
            triggerZ            = 0,
            triggerY            = -124920,
            triggerRange        = 1000,
            actorX              = 13480,
            actorZ              = 1500,
            actorY              = -124890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22010,
            triggerZ            = 0,
            triggerY            = -124520,
            triggerRange        = 1000,
            actorX              = 21700,
            actorZ              = 1500,
            actorY              = -125270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x292
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_29E'),
        (-1, 'loc_2B4'),
    )

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 3, 0x65B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B1',
    )

    SetScenaFlags(ScenaFlag(0x00CB, 3, 0x65B))
    Event(0, func_02_306)

    def _loc_2B1(): pass

    label('loc_2B1')

    Jump('loc_2B4')

    def _loc_2B4(): pass

    label('loc_2B4')

    Return()

# id: 0x0001 offset: 0x2B5
@scena.Code('func_01_2B5')
def func_01_2B5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 7, 0x6CF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C7',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2CE')

    def _loc_2C7(): pass

    label('loc_2C7')

    OP_6F(0x0000, 60)

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 0, 0x6D0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E0',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2E7')

    def _loc_2E0(): pass

    label('loc_2E0')

    OP_6F(0x0001, 60)

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 1, 0x6D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F9',
    )

    OP_6F(0x0002, 0)

    Jump('loc_300')

    def _loc_2F9(): pass

    label('loc_2F9')

    OP_6F(0x0002, 60)

    def _loc_300(): pass

    label('loc_300')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x306
@scena.Code('func_02_306')
def func_02_306():
    EventBegin(0x00)
    CameraMove(2390, 500, 6540, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0104, 2810, 1750, 7840, 180)
    ChrSetPos(0x0108, 3280, 2000, 9470, 180)
    ChrSetPos(0x0102, 2460, 2000, 9480, 180)

    @scena.Lambda('lambda_037E')
    def lambda_037E():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_037E')

    DispatchAsync2(0x0108, 0x0001, lambda_037E)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_038F')

    DispatchAsync2(0x0102, 0x0001, lambda_038F)

    @scena.Lambda('lambda_03A0')
    def lambda_03A0():
        ChrWalkTo(0x00FE, 2570, 0, 5860, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_03A0)

    @scena.Lambda('lambda_03BB')
    def lambda_03BB():
        ChrWalkTo(0x00FE, 2570, 0, 5860, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_03BB)

    @scena.Lambda('lambda_03D6')
    def lambda_03D6():
        ChrWalkTo(0x00FE, 3220, 0, 4520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_03D6)

    WaitForThreadExit(0x0104, 0x0001)

    @scena.Lambda('lambda_03F6')
    def lambda_03F6():
        ChrWalkTo(0x00FE, 930, 0, 4910, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_03F6)

    WaitForThreadExit(0x0104, 0x0001)
    ChrSetDirection(0x0104, 90, 400)
    WaitForThreadExit(0x0108, 0x0002)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0104,
        (
            '#0040131015V#030F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131016V呵呵，我们这就确认一下\n',
            '之前提到的隐藏水路的路线图吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131017V#012F#5P没错……\n',
            '不过先等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS019._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(50, 0, -1, -1)
    TalkSetChrName('金')

    Talk(
        (
            '#0080131018V',
            (TxtCtl.SetColor, 0x0),
            '#070F现在我们所处的位置\n',
            '是在左下角的楼梯标记处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131019V图中央标有『＝』的地方\n',
            '就是隐藏水路的入口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020131020V#012F对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131021V首先就到那里去，\n',
            '然后调查一下附近的墙壁吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_28(0x004D, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x5CF
@scena.Code('func_03_5CF')
def func_03_5CF():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 7, 0x6CF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01A8, 1)"),
            Expr.Return,
        ),
        'loc_647',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '不松口排骨',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D9, 7, 0x6CF))

    Jump('loc_6C2')

    def _loc_647(): pass

    label('loc_647')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '不松口排骨',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '不松口排骨',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_6C2(): pass

    label('loc_6C2')

    Jump('loc_6FB')

    def _loc_6C5(): pass

    label('loc_6C5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x40)
    def _loc_6FB(): pass

    label('loc_6FB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x709
@scena.Code('func_04_709')
def func_04_709():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 0, 0x6D0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_77F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 0, 0x6D0))

    Jump('loc_7F6')

    def _loc_77F(): pass

    label('loc_77F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_7F6(): pass

    label('loc_7F6')

    Jump('loc_82F')

    def _loc_7F9(): pass

    label('loc_7F9')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x41)
    def _loc_82F(): pass

    label('loc_82F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x83D
@scena.Code('func_05_83D')
def func_05_83D():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 1, 0x6D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_92D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_8B3',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 1, 0x6D1))

    Jump('loc_92A')

    def _loc_8B3(): pass

    label('loc_8B3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_92A(): pass

    label('loc_92A')

    Jump('loc_963')

    def _loc_92D(): pass

    label('loc_92D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x42)
    def _loc_963(): pass

    label('loc_963')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

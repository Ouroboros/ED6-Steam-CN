import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C2115_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2115   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2115.x'
    header.mapIndex       = 1
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
        ('ED6_DT09/CH10560._CH', 'ED6_DT09/CH10560P._CP'),
        ('ED6_DT09/CH10561._CH', 'ED6_DT09/CH10561P._CP'),
        ('ED6_DT09/CH10570._CH', 'ED6_DT09/CH10570P._CP'),
        ('ED6_DT09/CH10571._CH', 'ED6_DT09/CH10571P._CP'),
        ('ED6_DT09/CH10580._CH', 'ED6_DT09/CH10580P._CP'),
        ('ED6_DT09/CH10581._CH', 'ED6_DT09/CH10581P._CP'),
        ('ED6_DT09/CH10590._CH', 'ED6_DT09/CH10590P._CP'),
        ('ED6_DT09/CH10591._CH', 'ED6_DT09/CH10591P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 3970,
            z           = 0,
            y           = 3770,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BC,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x186
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x186
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -8230,
            triggerZ            = 0,
            triggerY            = 8330,
            triggerRange        = 1000,
            actorX              = -8730,
            actorZ              = 0,
            actorY              = 8830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9350,
            triggerZ            = 0,
            triggerY            = 9330,
            triggerRange        = 1000,
            actorX              = 8850,
            actorZ              = 0,
            actorY              = 8830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12530,
            triggerZ            = 0,
            triggerY            = -660,
            triggerRange        = 1000,
            actorX              = 12530,
            actorZ              = 0,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12430,
            triggerZ            = 0,
            triggerY            = -640,
            triggerRange        = 1000,
            actorX              = -12430,
            actorZ              = 0,
            actorY              = 110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4470,
            triggerZ            = 0,
            triggerY            = 22500,
            triggerRange        = 1000,
            actorX              = 4690,
            actorZ              = 0,
            actorY              = 23200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x23A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x23B
@scena.Code('func_01_23B')
def func_01_23B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0095, 6, 0x4AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_254')

    def _loc_24D(): pass

    label('loc_24D')

    OP_6F(0x0000, 60)

    def _loc_254(): pass

    label('loc_254')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 0, 0x4B0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_266',
    )

    OP_6F(0x0001, 0)

    Jump('loc_26D')

    def _loc_266(): pass

    label('loc_266')

    OP_6F(0x0001, 60)

    def _loc_26D(): pass

    label('loc_26D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 2, 0x4B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_286')

    def _loc_27F(): pass

    label('loc_27F')

    OP_6F(0x0002, 60)

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 4, 0x4B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298',
    )

    OP_6F(0x0003, 0)

    Jump('loc_29F')

    def _loc_298(): pass

    label('loc_298')

    OP_6F(0x0003, 60)

    def _loc_29F(): pass

    label('loc_29F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 6, 0x4B6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B1',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2B8')

    def _loc_2B1(): pass

    label('loc_2B1')

    OP_6F(0x0004, 60)

    def _loc_2B8(): pass

    label('loc_2B8')

    OP_25(0x01CB, -90, 0, 150, 2000, 25000, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x2D5
@scena.Code('func_02_2D5')
def func_02_2D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2EA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2D5')

    def _loc_2EA(): pass

    label('loc_2EA')

    Return()

# id: 0x0003 offset: 0x2EB
@scena.Code('func_03_2EB')
def func_03_2EB():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0095, 6, 0x4AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0095, 7, 0x4AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C7',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, -8730, 3000, 8830, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_033A')
    def lambda_033A():
        ChrMoveTo(0x00FE, -8730, 1500, 8830, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_033A)

    @scena.Lambda('lambda_0355')
    def lambda_0355():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0355)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_3A2'),
        (0x00000002, 'loc_3B4'),
        (0x00000001, 'loc_3C4'),
        (-1, 'loc_3C7'),
    )

    def _loc_3A2(): pass

    label('loc_3A2')

    SetScenaFlags(ScenaFlag(0x0095, 7, 0x4AF))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_3C7')

    def _loc_3B4(): pass

    label('loc_3B4')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_3C4(): pass

    label('loc_3C4')

    OP_B4(0x00)

    Return()

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.Eval, "AddItem(0x007B, 1)"),
            Expr.Return,
        ),
        'loc_41B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '水纹剑',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0095, 6, 0x4AE))

    Jump('loc_48C')

    def _loc_41B(): pass

    label('loc_41B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '水纹剑',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '水纹剑',
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

    def _loc_48C(): pass

    label('loc_48C')

    Jump('loc_4C5')

    def _loc_48F(): pass

    label('loc_48F')

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
    WaitEffect(0x0F, 0x20)
    def _loc_4C5(): pass

    label('loc_4C5')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4D3
@scena.Code('func_04_4D3')
def func_04_4D3():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 0, 0x4B0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_671',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 1, 0x4B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AF',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetPos(0x0009, 8850, 3000, 8830, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_0522')
    def lambda_0522():
        ChrMoveTo(0x00FE, 8850, 1500, 8830, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0522)

    @scena.Lambda('lambda_053D')
    def lambda_053D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_053D)

    ChrClearFlags(0x0009, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_58A'),
        (0x00000002, 'loc_59C'),
        (0x00000001, 'loc_5AC'),
        (-1, 'loc_5AF'),
    )

    def _loc_58A(): pass

    label('loc_58A')

    SetScenaFlags(ScenaFlag(0x0096, 1, 0x4B1))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_5AF')

    def _loc_59C(): pass

    label('loc_59C')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_5AC(): pass

    label('loc_5AC')

    OP_B4(0x00)

    Return()

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.Eval, "AddItem(0x02D0, 1)"),
            Expr.Return,
        ),
        'loc_601',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '异香',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0096, 0, 0x4B0))

    Jump('loc_66E')

    def _loc_601(): pass

    label('loc_601')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '异香',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '异香',
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

    def _loc_66E(): pass

    label('loc_66E')

    Jump('loc_6A7')

    def _loc_671(): pass

    label('loc_671')

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
    WaitEffect(0x0F, 0x21)
    def _loc_6A7(): pass

    label('loc_6A7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6B5
@scena.Code('func_05_6B5')
def func_05_6B5():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 2, 0x4B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_859',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 3, 0x4B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_791',
    )

    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetPos(0x000A, 12530, 3000, 0, 320)
    ChrTurnDirection(0x000A, 0x0000, 0)

    @scena.Lambda('lambda_0704')
    def lambda_0704():
        ChrMoveTo(0x00FE, 12530, 1500, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0704)

    @scena.Lambda('lambda_071F')
    def lambda_071F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_071F)

    ChrClearFlags(0x000A, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x000A, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_76C'),
        (0x00000002, 'loc_77E'),
        (0x00000001, 'loc_78E'),
        (-1, 'loc_791'),
    )

    def _loc_76C(): pass

    label('loc_76C')

    SetScenaFlags(ScenaFlag(0x0096, 3, 0x4B3))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_791')

    def _loc_77E(): pass

    label('loc_77E')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_78E(): pass

    label('loc_78E')

    OP_B4(0x00)

    Return()

    def _loc_791(): pass

    label('loc_791')

    If(
        (
            (Expr.Eval, "AddItem(0x00F9, 1)"),
            Expr.Return,
        ),
        'loc_7E5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0096, 2, 0x4B2))

    Jump('loc_856')

    def _loc_7E5(): pass

    label('loc_7E5')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
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

    def _loc_856(): pass

    label('loc_856')

    Jump('loc_88F')

    def _loc_859(): pass

    label('loc_859')

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
    WaitEffect(0x0F, 0x22)
    def _loc_88F(): pass

    label('loc_88F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x89D
@scena.Code('func_06_89D')
def func_06_89D():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 4, 0x4B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A41',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 5, 0x4B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_979',
    )

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetPos(0x000B, -12430, 3000, 110, 320)
    ChrTurnDirection(0x000B, 0x0000, 0)

    @scena.Lambda('lambda_08EC')
    def lambda_08EC():
        ChrMoveTo(0x00FE, -12430, 1500, 110, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_08EC)

    @scena.Lambda('lambda_0907')
    def lambda_0907():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0907)

    ChrClearFlags(0x000B, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000001BD, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x000B, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_954'),
        (0x00000002, 'loc_966'),
        (0x00000001, 'loc_976'),
        (-1, 'loc_979'),
    )

    def _loc_954(): pass

    label('loc_954')

    SetScenaFlags(ScenaFlag(0x0096, 5, 0x4B5))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_979')

    def _loc_966(): pass

    label('loc_966')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_976(): pass

    label('loc_976')

    OP_B4(0x00)

    Return()

    def _loc_979(): pass

    label('loc_979')

    If(
        (
            (Expr.Eval, "AddItem(0x0117, 1)"),
            Expr.Return,
        ),
        'loc_9CD',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '军用靴',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0096, 4, 0x4B4))

    Jump('loc_A3E')

    def _loc_9CD(): pass

    label('loc_9CD')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '军用靴',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '军用靴',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_A3E(): pass

    label('loc_A3E')

    Jump('loc_A77')

    def _loc_A41(): pass

    label('loc_A41')

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
    WaitEffect(0x0F, 0x23)
    def _loc_A77(): pass

    label('loc_A77')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA85
@scena.Code('func_07_A85')
def func_07_A85():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0096, 6, 0x4B6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FE, 1)"),
            Expr.Return,
        ),
        'loc_AFD',
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
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0096, 6, 0x4B6))

    Jump('loc_B78')

    def _loc_AFD(): pass

    label('loc_AFD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ填充剂',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_B78(): pass

    label('loc_B78')

    Jump('loc_BB1')

    def _loc_B7B(): pass

    label('loc_B7B')

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
    WaitEffect(0x0F, 0x24)
    def _loc_BB1(): pass

    label('loc_BB1')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

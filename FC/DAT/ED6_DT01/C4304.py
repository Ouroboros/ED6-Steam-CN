import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4304   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4304.x'
    header.mapIndex       = 216
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA73
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
        ('ED6_DT09/CH11090._CH', 'ED6_DT09/CH11090P._CP'),
        ('ED6_DT09/CH11091._CH', 'ED6_DT09/CH11091P._CP'),
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT09/CH11001._CH', 'ED6_DT09/CH11001P._CP'),
        ('ED6_DT09/CH10930._CH', None),
        ('ED6_DT09/CH10931._CH', None),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xF2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -3060,
            z           = 0,
            y           = 75060,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -13240,
            z           = 0,
            y           = 150640,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 135180,
            z           = 0,
            y           = 146710,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 64840,
            z           = 0,
            y           = 273920,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23360,
            z           = 0,
            y           = 233960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -159380,
            z           = 0,
            y           = 159140,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -303150,
            triggerZ            = 0,
            triggerY            = 178540,
            triggerRange        = 1000,
            actorX              = -302930,
            actorZ              = 0,
            actorY              = 179190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 64950,
            triggerZ            = 0,
            triggerY            = 274130,
            triggerRange        = 1000,
            actorX              = 64980,
            actorZ              = 0,
            actorY              = 274850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 130900,
            triggerZ            = 0,
            triggerY            = 152640,
            triggerRange        = 1000,
            actorX              = 130930,
            actorZ              = 0,
            actorY              = 153290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -154890,
            triggerZ            = 0,
            triggerY            = 158890,
            triggerRange        = 1000,
            actorX              = -154240,
            actorZ              = 0,
            actorY              = 158990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -177340,
            triggerZ            = 0,
            triggerY            = 241160,
            triggerRange        = 1000,
            actorX              = -178080,
            actorZ              = 0,
            actorY              = 241020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x24F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 0, 0x6C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_261',
    )

    OP_6F(0x0000, 0)

    Jump('loc_268')

    def _loc_261(): pass

    label('loc_261')

    OP_6F(0x0000, 60)

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 2, 0x6CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27A',
    )

    OP_6F(0x0002, 0)

    Jump('loc_281')

    def _loc_27A(): pass

    label('loc_27A')

    OP_6F(0x0002, 60)

    def _loc_281(): pass

    label('loc_281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 4, 0x6CC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_293',
    )

    OP_6F(0x0001, 0)

    Jump('loc_29A')

    def _loc_293(): pass

    label('loc_293')

    OP_6F(0x0001, 60)

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 5, 0x6CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AC',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2B3')

    def _loc_2AC(): pass

    label('loc_2AC')

    OP_6F(0x0003, 60)

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 6, 0x6CE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C5',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2CC')

    def _loc_2C5(): pass

    label('loc_2C5')

    OP_6F(0x0004, 60)

    def _loc_2CC(): pass

    label('loc_2CC')

    Return()

# id: 0x0002 offset: 0x2CD
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E2',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2E2(): pass

    label('loc_2E2')

    Return()

# id: 0x0003 offset: 0x2E3
@scena.Code('func_03_2E3')
def func_03_2E3():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 0, 0x6C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 1, 0x6C9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C3',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, -302930, 1500, 179190, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0332')
    def lambda_0332():
        ChrMoveTo(0x00FE, -302930, 1000, 179190, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0332)

    @scena.Lambda('lambda_034D')
    def lambda_034D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_034D)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000030F, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_39E'),
        (0x00000002, 'loc_3B0'),
        (0x00000001, 'loc_3C0'),
        (-1, 'loc_3C3'),
    )

    def _loc_39E(): pass

    label('loc_39E')

    SetScenaFlags(ScenaFlag(0x00D9, 1, 0x6C9))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_3C3')

    def _loc_3B0(): pass

    label('loc_3B0')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_3C0(): pass

    label('loc_3C0')

    OP_B4(0x00)

    Return()

    def _loc_3C3(): pass

    label('loc_3C3')

    If(
        (
            (Expr.Eval, "AddItem(0x00D9, 1)"),
            Expr.Return,
        ),
        'loc_41D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '代达罗斯护腕',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D9, 0, 0x6C8))

    Jump('loc_49A')

    def _loc_41D(): pass

    label('loc_41D')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '代达罗斯护腕',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '代达罗斯护腕',
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

    def _loc_49A(): pass

    label('loc_49A')

    Jump('loc_4D3')

    def _loc_49D(): pass

    label('loc_49D')

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
    WaitEffect(0x0F, 0x4E)
    def _loc_4D3(): pass

    label('loc_4D3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4E1
@scena.Code('func_04_4E1')
def func_04_4E1():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 2, 0x6CA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 3, 0x6CB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C1',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, 64980, 1500, 274850, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0530')
    def lambda_0530():
        ChrMoveTo(0x00FE, 64980, 1000, 274850, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0530)

    @scena.Lambda('lambda_054B')
    def lambda_054B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_054B)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x0000030F, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_59C'),
        (0x00000002, 'loc_5AE'),
        (0x00000001, 'loc_5BE'),
        (-1, 'loc_5C1'),
    )

    def _loc_59C(): pass

    label('loc_59C')

    SetScenaFlags(ScenaFlag(0x00D9, 3, 0x6CB))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_5C1')

    def _loc_5AE(): pass

    label('loc_5AE')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_5BE(): pass

    label('loc_5BE')

    OP_B4(0x00)

    Return()

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.Eval, "AddItem(0x0062, 1)"),
            Expr.Return,
        ),
        'loc_617',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '王权之光',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D9, 2, 0x6CA))

    Jump('loc_68C')

    def _loc_617(): pass

    label('loc_617')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '王权之光',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '王权之光',
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

    def _loc_68C(): pass

    label('loc_68C')

    Jump('loc_6C5')

    def _loc_68F(): pass

    label('loc_68F')

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
    WaitEffect(0x0F, 0x4F)
    def _loc_6C5(): pass

    label('loc_6C5')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6D3
@scena.Code('func_05_6D3')
def func_05_6D3():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 4, 0x6CC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7BD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_747',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D9, 4, 0x6CC))

    Jump('loc_7BA')

    def _loc_747(): pass

    label('loc_747')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
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

    def _loc_7BA(): pass

    label('loc_7BA')

    Jump('loc_7F3')

    def _loc_7BD(): pass

    label('loc_7BD')

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
    WaitEffect(0x0F, 0x50)
    def _loc_7F3(): pass

    label('loc_7F3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x801
@scena.Code('func_06_801')
def func_06_801():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 5, 0x6CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8EB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_875',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D9, 5, 0x6CD))

    Jump('loc_8E8')

    def _loc_875(): pass

    label('loc_875')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
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

    def _loc_8E8(): pass

    label('loc_8E8')

    Jump('loc_921')

    def _loc_8EB(): pass

    label('loc_8EB')

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
    WaitEffect(0x0F, 0x51)
    def _loc_921(): pass

    label('loc_921')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x92F
@scena.Code('func_07_92F')
def func_07_92F():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D9, 6, 0x6CE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A1F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_9A5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    SetScenaFlags(ScenaFlag(0x00D9, 6, 0x6CE))

    Jump('loc_A1C')

    def _loc_9A5(): pass

    label('loc_9A5')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_A1C(): pass

    label('loc_A1C')

    Jump('loc_A55')

    def _loc_A1F(): pass

    label('loc_A1F')

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
    WaitEffect(0x0F, 0x52)
    def _loc_A55(): pass

    label('loc_A55')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

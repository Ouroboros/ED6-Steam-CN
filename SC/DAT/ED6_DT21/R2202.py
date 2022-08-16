import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2202   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2202.x'
    header.mapIndex       = 101
    header.bgm            = 29
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH11060._CH', 'ED6_DT09/CH11060P._CP'),
        ('ED6_DT09/CH11061._CH', 'ED6_DT09/CH11061P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT29/CH12100._CH', 'ED6_DT29/CH12100P._CP'),
        ('ED6_DT29/CH12101._CH', 'ED6_DT29/CH12101P._CP'),
        ('ED6_DT29/CH12150._CH', 'ED6_DT29/CH12150P._CP'),
        ('ED6_DT29/CH12151._CH', 'ED6_DT29/CH12151P._CP'),
        ('ED6_DT29/CH12160._CH', 'ED6_DT29/CH12160P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 137480,
            z                   = -2000,
            y                   = -212630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卢安方向',
            x                   = 146110,
            z                   = -2000,
            y                   = -272220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '街景林道',
            x                   = 195320,
            z                   = -2000,
            y                   = -200020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚村方向',
            x                   = 117860,
            z                   = -1990,
            y                   = -86810,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 108600,
            z           = -2090,
            y           = -127120,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x017D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 127020,
            z           = -2029,
            y           = -168530,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0183,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 131400,
            z           = -1930,
            y           = -226630,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x017E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 136960,
            z           = -2020,
            y           = -153050,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0183,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 123750,
            z           = -6120,
            y           = -163430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0189,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 113340,
            z           = -6030,
            y           = -111320,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0189,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 107810,
            z           = -6150,
            y           = -227590,
            word_0C     = 0x00B4,
            word_0E     = 0x0010,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x286
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 171570,
            y           = -3000,
            z           = -204390,
            range       = 173310,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFD053A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = 132230,
            y           = -3000,
            z           = -209630,
            range       = 142840,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFCB5B2,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x2C6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 123800,
            triggerZ            = -6110,
            triggerY            = -164160,
            triggerRange        = 1000,
            actorX              = 123890,
            actorZ              = -6040,
            actorY              = -164820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110610,
            triggerZ            = -2050,
            triggerY            = -169010,
            triggerRange        = 1000,
            actorX              = 111270,
            actorZ              = -1960,
            actorY              = -169020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 114670,
            triggerZ            = -6010,
            triggerY            = -111030,
            triggerRange        = 1000,
            actorX              = 115310,
            actorZ              = -5950,
            actorY              = -111030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 145130,
            triggerZ            = -2029,
            triggerY            = -194770,
            triggerRange        = 1500,
            actorX              = 145130,
            actorZ              = -500,
            actorY              = -194770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 143160,
            triggerZ            = -1960,
            triggerY            = -203990,
            triggerRange        = 1500,
            actorX              = 143160,
            actorZ              = -550,
            actorY              = -203990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110290,
            triggerZ            = -6670,
            triggerY            = -241280,
            triggerRange        = 1000,
            actorX              = 109660,
            actorZ              = -6650,
            actorY              = -244800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x39E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x39F
@scena.Code('func_01_39F')
def func_01_39F():
    OP_16(0x02, 4000, 10000, -311000, 2293800)
    PlaySE(456, 0x01, 0x64)

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x1900),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 7, 0x1307)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3E4')

    def _loc_3DD(): pass

    label('loc_3DD')

    OP_6F(0x0001, 60)

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 0, 0x1308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_6F(0x0002, 0)

    Jump('loc_3FD')

    def _loc_3F6(): pass

    label('loc_3F6')

    OP_6F(0x0002, 60)

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 1, 0x1309)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_6F(0x0003, 0)

    Jump('loc_416')

    def _loc_40F(): pass

    label('loc_40F')

    OP_6F(0x0003, 60)

    def _loc_416(): pass

    label('loc_416')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_445',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_430',
    )

    ChrSetDirection(0x0008, 180, 0)

    def _loc_430(): pass

    label('loc_430')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 2, 0x20FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_442',
    )

    ChrClearFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_442(): pass

    label('loc_442')

    Jump('loc_44F')

    def _loc_445(): pass

    label('loc_445')

    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    def _loc_44F(): pass

    label('loc_44F')

    Return()

# id: 0x0002 offset: 0x450
@scena.Code('func_02_450')
def func_02_450():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_465',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_450')

    def _loc_465(): pass

    label('loc_465')

    Return()

# id: 0x0003 offset: 0x466
@scena.Code('func_03_466')
def func_03_466():
    UnlockAchievement(0x02, 0x01E5, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 7, 0x1307)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_543',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_4DA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0260, 7, 0x1307))

    Jump('loc_540')

    def _loc_4DA(): pass

    label('loc_4DA')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
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

    def _loc_540(): pass

    label('loc_540')

    Jump('loc_574')

    def _loc_543(): pass

    label('loc_543')

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
    def _loc_574(): pass

    label('loc_574')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x582
@scena.Code('func_04_582')
def func_04_582():
    UnlockAchievement(0x02, 0x01E6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 0, 0x1308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_5F6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0261, 0, 0x1308))

    Jump('loc_65C')

    def _loc_5F6(): pass

    label('loc_5F6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_65C(): pass

    label('loc_65C')

    Jump('loc_690')

    def _loc_65F(): pass

    label('loc_65F')

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
    def _loc_690(): pass

    label('loc_690')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x69E
@scena.Code('func_05_69E')
def func_05_69E():
    UnlockAchievement(0x02, 0x01E7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 1, 0x1309)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_77B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大吃一惊曲奇饼'], 1)"),
            Expr.Return,
        ),
        'loc_712',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0261, 1, 0x1309))

    Jump('loc_778')

    def _loc_712(): pass

    label('loc_712')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_778(): pass

    label('loc_778')

    Jump('loc_7AC')

    def _loc_77B(): pass

    label('loc_77B')

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
    def _loc_7AC(): pass

    label('loc_7AC')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_804',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0014)"),
            Expr.Return,
        ),
        'loc_7CB',
    )

    Jump('loc_804')

    def _loc_7CB(): pass

    label('loc_7CB')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['大吃一惊曲奇饼']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_804(): pass

    label('loc_804')

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x80D
@scena.Code('func_06_80D')
def func_06_80D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9AD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_8E1',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050430287V#050F这么说来\n',
            '还有拍摄的工作没处理完啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430288V还是先做完比较好吧。\n',
            '因为调查时间或许会拖得很长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430289V#1015F啊，嗯。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_992')

    def _loc_8E1(): pass

    label('loc_8E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_992',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030430290V#020F这么说来还有\n',
            '拍摄的工作没处理完呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430291V先做完怎么样？\n',
            '调查时间或许会拖得很长哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430289V#1015F啊，嗯。\n',
            '那样也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_992(): pass

    label('loc_992')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_9AD(): pass

    label('loc_9AD')

    Return()

# id: 0x0007 offset: 0x9AE
@scena.Code('func_07_9AE')
def func_07_9AE():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　杰尼丝王立学院　２５２塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xA01
@scena.Code('func_08_A01')
def func_08_A01():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　卢安市\n',
            '北　玛诺利亚村　　　３１２塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xA5F
@scena.Code('func_09_A5F')
def func_09_A5F():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_A73'),
        (0x00000065, 'loc_A73'),
        (0x00000066, 'loc_BC5'),
        (-1, 'loc_D17'),
    )

    def _loc_A73(): pass

    label('loc_A73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 2, 0x20FA)),
            Expr.Return,
        ),
        'loc_A7B',
    )

    Return()

    def _loc_A7B(): pass

    label('loc_A7B')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_B60'),
        (-1, 'loc_B83'),
    )

    def _loc_B60(): pass

    label('loc_B60')

    Fade(500)
    OP_89(0x0000, 137640, -2000, -205720, 180)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_B83(): pass

    label('loc_B83')

    Battle(0x00000EF1, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 137640, -2000, -205720, 180)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_BBC'),
        (0x00000001, 'loc_BBF'),
        (-1, 'loc_BC2'),
    )

    def _loc_BBC(): pass

    label('loc_BBC')

    EventEnd(0x00)

    Return()

    def _loc_BBF(): pass

    label('loc_BBF')

    OP_B4(0x00)

    Return()

    def _loc_BC2(): pass

    label('loc_BC2')

    Jump('loc_D17')

    def _loc_BC5(): pass

    label('loc_BC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 2, 0x20FA)),
            Expr.Return,
        ),
        'loc_BCD',
    )

    Return()

    def _loc_BCD(): pass

    label('loc_BCD')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_CB2'),
        (-1, 'loc_CD5'),
    )

    def _loc_CB2(): pass

    label('loc_CB2')

    Fade(500)
    OP_89(0x0000, 137360, -2000, -219630, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_CD5(): pass

    label('loc_CD5')

    Battle(0x00000EF9, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 137360, -2000, -219630, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_D0E'),
        (0x00000001, 'loc_D11'),
        (-1, 'loc_D14'),
    )

    def _loc_D0E(): pass

    label('loc_D0E')

    EventEnd(0x00)

    Return()

    def _loc_D11(): pass

    label('loc_D11')

    OP_B4(0x00)

    Return()

    def _loc_D14(): pass

    label('loc_D14')

    Jump('loc_D17')

    def _loc_D17(): pass

    label('loc_D17')

    EventBegin(0x01)
    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x041F, 2, 0x20FA))
    OP_28(0x00B9, 0x04, 0x10)
    OP_28(0x00B9, 0x04, 0x02)
    OP_28(0x00B9, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xD83
@scena.Code('func_0A_D83')
def func_0A_D83():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DBB')
    def lambda_0DBB():
        CameraMove(109750, -6680, -243120, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DBB)

    @scena.Lambda('lambda_0DD3')
    def lambda_0DD3():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0DD3)

    @scena.Lambda('lambda_0DE3')
    def lambda_0DE3():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0DE3)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
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
            TXT(0x00, '钓鱼\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E6A',
    )

    OP_C0(0x0E, 0x00000017, 0x0001AED2, 0xFFFFE5F2, 0xFFFC5180, 0x000000B4, 0x0001AC16, 0xFFFFE958, 0xFFFC406E)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_E79')

    def _loc_E6A(): pass

    label('loc_E6A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E79',
    )

    EventEnd(0x01)

    def _loc_E79(): pass

    label('loc_E79')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

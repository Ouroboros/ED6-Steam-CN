import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1306_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1306   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1306.x'
    header.mapIndex       = 52
    header.bgm            = 89
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
        ('ED6_DT09/CH10380._CH', 'ED6_DT09/CH10380P._CP'),
        ('ED6_DT09/CH10381._CH', 'ED6_DT09/CH10381P._CP'),
        ('ED6_DT09/CH10390._CH', 'ED6_DT09/CH10390P._CP'),
        ('ED6_DT09/CH10391._CH', 'ED6_DT09/CH10391P._CP'),
        ('ED6_DT09/CH10250._CH', 'ED6_DT09/CH10250P._CP'),
        ('ED6_DT09/CH10251._CH', 'ED6_DT09/CH10251P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '投发烟筒的人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310724,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '接发烟筒的人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310724,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -57220,
            z           = 0,
            y           = -50730,
            word_0C     = 0x00B3,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x156
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x156
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -142790,
            triggerZ            = 0,
            triggerY            = 58560,
            triggerRange        = 1000,
            actorX              = -142760,
            actorZ              = 1500,
            actorY              = 59200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -55470,
            triggerZ            = 0,
            triggerY            = -105270,
            triggerRange        = 1000,
            actorX              = -54920,
            actorZ              = 1500,
            actorY              = -105280,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -102030,
            triggerZ            = 0,
            triggerY            = -40370,
            triggerRange        = 1000,
            actorX              = -101990,
            actorZ              = 0,
            actorY              = -39700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -990,
            triggerZ            = 0,
            triggerY            = -145880,
            triggerRange        = 800,
            actorX              = -990,
            actorZ              = 800,
            actorY              = -145880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1F8',
    )

    OP_64(0x03, 0x0001)
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_06_5C0)

    def _loc_1F8(): pass

    label('loc_1F8')

    Return()

# id: 0x0001 offset: 0x1F9
@scena.Code('func_01_1F9')
def func_01_1F9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 1, 0x1901)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B',
    )

    OP_6F(0x0002, 0)

    Jump('loc_212')

    def _loc_20B(): pass

    label('loc_20B')

    OP_6F(0x0002, 60)

    def _loc_212(): pass

    label('loc_212')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 2, 0x1902)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_224',
    )

    OP_6F(0x0003, 0)

    Jump('loc_22B')

    def _loc_224(): pass

    label('loc_224')

    OP_6F(0x0003, 60)

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 3, 0x1903)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23D',
    )

    OP_6F(0x0004, 0)

    Jump('loc_244')

    def _loc_23D(): pass

    label('loc_23D')

    OP_6F(0x0004, 60)

    def _loc_244(): pass

    label('loc_244')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 2, 0x1802)),
            Expr.Return,
        ),
        'loc_252',
    )

    OP_64(0x03, 0x0001)

    Jump('loc_257')

    def _loc_252(): pass

    label('loc_252')

    OP_72(0x0000, 0x0010)

    def _loc_257(): pass

    label('loc_257')

    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0002 offset: 0x25D
@scena.Code('func_02_25D')
def func_02_25D():
    UnlockAchievement(0x02, 0x0050, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 1, 0x1901)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_2D1',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0320, 1, 0x1901))

    Jump('loc_337')

    def _loc_2D1(): pass

    label('loc_2D1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_337(): pass

    label('loc_337')

    Jump('loc_36B')

    def _loc_33A(): pass

    label('loc_33A')

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
    def _loc_36B(): pass

    label('loc_36B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x379
@scena.Code('func_03_379')
def func_03_379():
    UnlockAchievement(0x02, 0x0051, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 2, 0x1902)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_3ED',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0320, 2, 0x1902))

    Jump('loc_453')

    def _loc_3ED(): pass

    label('loc_3ED')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
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

    def _loc_453(): pass

    label('loc_453')

    Jump('loc_487')

    def _loc_456(): pass

    label('loc_456')

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
    def _loc_487(): pass

    label('loc_487')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x495
@scena.Code('func_04_495')
def func_04_495():
    UnlockAchievement(0x02, 0x0052, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0320, 3, 0x1903)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_572',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_509',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0320, 3, 0x1903))

    Jump('loc_56F')

    def _loc_509(): pass

    label('loc_509')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_56F(): pass

    label('loc_56F')

    Jump('loc_5A3')

    def _loc_572(): pass

    label('loc_572')

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
    def _loc_5A3(): pass

    label('loc_5A3')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5B1
@scena.Code('func_05_5B1')
def func_05_5B1():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1304._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x5C0
@scena.Code('func_06_5C0')
def func_06_5C0():
    EventBegin(0x00)
    CameraMove(-970, 0, -146920, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, -1280, 0, -146530, 0)
    ChrSetPos(0x0146, -2570, 0, -147040, 90)
    ChrSetPos(0x0129, -320, 0, -147490, 0)
    ChrSetPos(0x012A, -1440, 0, -147850, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0129,
        (
            '#0300280192V#190F（喂……怎么样？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280193V#1033F#5P（不妙啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 500)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020280194V#1030F#5P（吉尔，能给一个\n',
            '我给你的Ｓ２弾吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280195V#201F（哦，哦哦……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x012A, -1420, 0, -147400, 2000, 0x00)
    Sleep(1000)

    ChrMoveTo(0x012A, -1430, 0, -147850, 2000, 0x00)
    ChrSetDirection(0x0102, 0, 400)
    Fade(500)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 6)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C1304._SN', 101, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0414_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0414   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0414.x'
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
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10070._CH', 'ED6_DT09/CH10070P._CP'),
        ('ED6_DT09/CH10071._CH', 'ED6_DT09/CH10071P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
        ('ED6_DT09/CH10190._CH', 'ED6_DT09/CH10190P._CP'),
        ('ED6_DT09/CH10191._CH', 'ED6_DT09/CH10191P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 4420,
            z                   = 1000,
            y                   = -23090,
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

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -14210,
            z           = 0,
            y           = 14100,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0033,
            word_18     = 0x1976,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -40,
            z           = 0,
            y           = 4100,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x1977,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 4019,
            z           = 0,
            y           = -4000,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0032,
            word_18     = 0x1978,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -3950,
            z           = 0,
            y           = -4080,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0033,
            word_18     = 0x1979,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -2610,
            z           = 0,
            y           = -20030,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x197A,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1A6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1A6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4370,
            triggerZ            = 0,
            triggerY            = -22480,
            triggerRange        = 1000,
            actorX              = 4420,
            actorZ              = 0,
            actorY              = -23090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1CA
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x1CB
@scena.Code('func_01_1CB')
def func_01_1CB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 6, 0x1956)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1E4')

    def _loc_1DD(): pass

    label('loc_1DD')

    OP_6F(0x0000, 60)

    def _loc_1E4(): pass

    label('loc_1E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 6, 0x1976)),
            Expr.Return,
        ),
        'loc_1F0',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_1F0(): pass

    label('loc_1F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032E, 7, 0x1977)),
            Expr.Return,
        ),
        'loc_1FC',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_1FC(): pass

    label('loc_1FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032F, 0, 0x1978)),
            Expr.Return,
        ),
        'loc_208',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_208(): pass

    label('loc_208')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032F, 1, 0x1979)),
            Expr.Return,
        ),
        'loc_214',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_214(): pass

    label('loc_214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032F, 2, 0x197A)),
            Expr.Return,
        ),
        'loc_220',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_220(): pass

    label('loc_220')

    Return()

# id: 0x0002 offset: 0x221
@scena.Code('func_02_221')
def func_02_221():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_236',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_221')

    def _loc_236(): pass

    label('loc_236')

    Return()

# id: 0x0003 offset: 0x237
@scena.Code('func_03_237')
def func_03_237():
    UnlockAchievement(0x02, 0x01FF, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 6, 0x1956)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032A, 7, 0x1957)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31B',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_028E')
    def lambda_028E():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_028E)

    @scena.Lambda('lambda_02A9')
    def lambda_02A9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_02A9)

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
    Battle(0x00000035, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_2F6'),
        (0x00000002, 'loc_308'),
        (0x00000001, 'loc_318'),
        (-1, 'loc_31B'),
    )

    def _loc_2F6(): pass

    label('loc_2F6')

    SetScenaFlags(ScenaFlag(0x032A, 7, 0x1957))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_31B')

    def _loc_308(): pass

    label('loc_308')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_318(): pass

    label('loc_318')

    OP_B4(0x00)

    Return()

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['女术士战袍'], 1)"),
            Expr.Return,
        ),
        'loc_36A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['女术士战袍']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032A, 6, 0x1956))

    Jump('loc_3CC')

    def _loc_36A(): pass

    label('loc_36A')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['女术士战袍']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['女术士战袍']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_3CC(): pass

    label('loc_3CC')

    Jump('loc_3FE')

    def _loc_3CF(): pass

    label('loc_3CF')

    FadeOut(300, 0, 100)

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
    def _loc_3FE(): pass

    label('loc_3FE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

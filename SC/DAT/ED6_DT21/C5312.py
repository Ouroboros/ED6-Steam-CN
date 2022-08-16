import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5312_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5312   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5312.x'
    header.mapIndex       = 1
    header.bgm            = 64
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
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -80,
            z                   = 1500,
            y                   = 27600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = -27660,
            z                   = 91500,
            y                   = -1030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -40,
            triggerZ            = 0,
            triggerY            = 28300,
            triggerRange        = 1000,
            actorX              = -80,
            actorZ              = 0,
            actorY              = 27600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28370,
            triggerZ            = 90000,
            triggerY            = -1030,
            triggerRange        = 1000,
            actorX              = -27660,
            actorZ              = 90000,
            actorY              = -1030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x142
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x143
@scena.Code('func_01_143')
def func_01_143():
    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 0, 0x2360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15A',
    )

    OP_6F(0x0000, 0)

    Jump('loc_161')

    def _loc_15A(): pass

    label('loc_15A')

    OP_6F(0x0000, 60)

    def _loc_161(): pass

    label('loc_161')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 2, 0x2362)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_173',
    )

    OP_6F(0x0001, 0)

    Jump('loc_17A')

    def _loc_173(): pass

    label('loc_173')

    OP_6F(0x0001, 60)

    def _loc_17A(): pass

    label('loc_17A')

    Return()

# id: 0x0002 offset: 0x17B
@scena.Code('func_02_17B')
def func_02_17B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_190',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_17B')

    def _loc_190(): pass

    label('loc_190')

    Return()

# id: 0x0003 offset: 0x191
@scena.Code('func_03_191')
def func_03_191():
    UnlockAchievement(0x02, 0x0205, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 0, 0x2360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_329',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 1, 0x2361)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_275',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_01E8')
    def lambda_01E8():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_01E8)

    @scena.Lambda('lambda_0203')
    def lambda_0203():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0203)

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
    Battle(0x00000532, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_250'),
        (0x00000002, 'loc_262'),
        (0x00000001, 'loc_272'),
        (-1, 'loc_275'),
    )

    def _loc_250(): pass

    label('loc_250')

    SetScenaFlags(ScenaFlag(0x046C, 1, 0x2361))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_275')

    def _loc_262(): pass

    label('loc_262')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_272(): pass

    label('loc_272')

    OP_B4(0x00)

    Return()

    def _loc_275(): pass

    label('loc_275')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['斗神'], 1)"),
            Expr.Return,
        ),
        'loc_2C4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['斗神']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046C, 0, 0x2360))

    Jump('loc_326')

    def _loc_2C4(): pass

    label('loc_2C4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['斗神']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['斗神']),
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

    def _loc_326(): pass

    label('loc_326')

    Jump('loc_358')

    def _loc_329(): pass

    label('loc_329')

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
    def _loc_358(): pass

    label('loc_358')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x366
@scena.Code('func_04_366')
def func_04_366():
    UnlockAchievement(0x02, 0x0206, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 2, 0x2362)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x046C, 3, 0x2363)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44A',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0009, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0009, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_03BD')
    def lambda_03BD():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_03BD)

    @scena.Lambda('lambda_03D8')
    def lambda_03D8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_03D8)

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
    Battle(0x00000532, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_425'),
        (0x00000002, 'loc_437'),
        (0x00000001, 'loc_447'),
        (-1, 'loc_44A'),
    )

    def _loc_425(): pass

    label('loc_425')

    SetScenaFlags(ScenaFlag(0x046C, 3, 0x2363))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_44A')

    def _loc_437(): pass

    label('loc_437')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_447(): pass

    label('loc_447')

    OP_B4(0x00)

    Return()

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['普罗米修斯神靴'], 1)"),
            Expr.Return,
        ),
        'loc_499',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['普罗米修斯神靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x046C, 2, 0x2362))

    Jump('loc_4FB')

    def _loc_499(): pass

    label('loc_499')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['普罗米修斯神靴']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['普罗米修斯神靴']),
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

    def _loc_4FB(): pass

    label('loc_4FB')

    Jump('loc_52D')

    def _loc_4FE(): pass

    label('loc_4FE')

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
    def _loc_52D(): pass

    label('loc_52D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '庭园大道方向'),
    TXT(0x02, '艾尔贝离宫方向'),
    TXT(0x03, '炽炎草3'),
    TXT(0x04, '贪婪鳄鱼4'),
    TXT(0x05, '凶暴巨鳄3'),
    TXT(0x06, '好战蝙蝠6'),
    TXT(0x07, '迅猛小鹫3'),
    TXT(0x08, '地狱火爆麻雀3'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4100.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x814
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 980,
            z                   = 0,
            y                   = 71400,
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
            x                   = -43080,
            z                   = 0,
            y                   = -63930,
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

# id: 0x10003 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 11100,
            z           = -20,
            y           = 24620,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0262,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6780,
            z           = 40,
            y           = 21320,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0265,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2830,
            z           = 0,
            y           = -29020,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0264,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -50760,
            z           = 0,
            y           = 12800,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0266,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -44310,
            z           = 30,
            y           = -2880,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0268,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34560,
            z           = 170,
            y           = 8670,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0267,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -34880,
            triggerZ            = 80,
            triggerY            = 3840,
            triggerRange        = 1000,
            actorX              = -34320,
            actorZ              = 1590,
            actorY              = 3790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11000,
            triggerZ            = 0,
            triggerY            = -39890,
            triggerRange        = 1000,
            actorX              = -11070,
            actorZ              = 0,
            actorY              = -40530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -44400,
            triggerZ            = 500,
            triggerY            = 7650,
            triggerRange        = 1500,
            actorX              = -44400,
            actorZ              = 4000,
            actorY              = 7650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27E
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_28A'),
        (-1, 'loc_2A0'),
    )

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 5, 0x615)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29D',
    )

    SetScenaFlags(ScenaFlag(0x00C2, 5, 0x615))
    Event(0, 0x0002)

    def _loc_29D(): pass

    label('loc_29D')

    Jump('loc_2A0')

    def _loc_2A0(): pass

    label('loc_2A0')

    Return()

# id: 0x0001 offset: 0x2A1
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -138000, -128000, 196707)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 2, 0x682)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C5',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2CC')

    def _loc_2C5(): pass

    label('loc_2C5')

    OP_6F(0x0003, 60)

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 3, 0x683)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DE',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2E5')

    def _loc_2DE(): pass

    label('loc_2DE')

    OP_6F(0x0004, 60)

    def _loc_2E5(): pass

    label('loc_2E5')

    Return()

# id: 0x0002 offset: 0x2E6
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(750, 0, 48230, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -90, 0, 52000, 270)
    SetChrPos(0x0102, 1380, 0, 52150, 270)

    @scena.Lambda('lambda_034D')
    def lambda_034D():
        CameraMove(750, 0, 45230, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_034D)

    @scena.Lambda('lambda_0365')
    def lambda_0365():
        ChrWalkTo(0x00FE, 280, 0, 46340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0365)

    @scena.Lambda('lambda_0380')
    def lambda_0380():
        ChrWalkTo(0x00FE, 1650, 0, 46710, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0380)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010101345V#501F这就是艾尔贝周游道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101346V在森林中有用石头铺成的大路，\n',
            '真是有趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101347V#010F作为王都市民休憩的场所，\n',
            '好像是很久之前就建造的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101348V大概，已经有数百年的历史了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101349V#000F嗯……\n',
            '不愧是女王的脚下啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101350V#505F不过，怎么感觉有魔兽的气息呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101351V#015F真是敏锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101352V#012F我也感觉到这里\n',
            '有比刚才路上更厉害的魔兽呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101353V一边保持警惕一边找金先生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x55E
@scena.Code('func_03_55E')
def func_03_55E():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 2, 0x682)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0287, 1)"),
            Expr.Return,
        ),
        'loc_5D4',
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
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D0, 2, 0x682))

    Jump('loc_64B')

    def _loc_5D4(): pass

    label('loc_5D4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
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

    def _loc_64B(): pass

    label('loc_64B')

    Jump('loc_684')

    def _loc_64E(): pass

    label('loc_64E')

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
    WaitEffect(0x0F, 0x3B)
    def _loc_684(): pass

    label('loc_684')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x692
@scena.Code('func_04_692')
def func_04_692():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 3, 0x683)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_782',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_708',
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
    SetScenaFlags(ScenaFlag(0x00D0, 3, 0x683))

    Jump('loc_77F')

    def _loc_708(): pass

    label('loc_708')

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

    def _loc_77F(): pass

    label('loc_77F')

    Jump('loc_7B8')

    def _loc_782(): pass

    label('loc_782')

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
    WaitEffect(0x0F, 0x3C)
    def _loc_7B8(): pass

    label('loc_7B8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7C6
@scena.Code('func_05_7C6')
def func_05_7C6():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的翠耀石石碑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
